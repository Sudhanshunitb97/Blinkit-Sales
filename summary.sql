WITH orders_clean AS (
  SELECT
    o.order_id,
    o.customer_id,
    o.product_id,
    o.revenue,
    o.delivery_fee,
    o.is_returned,
    IF(o.is_returned = 1, -2 * o.delivery_fee, o.revenue - o.delivery_fee) AS net_profit
  FROM ecom.orders o
),

returns_summary AS (
  SELECT
    c.city_tier,
    c.is_loyalty_member,
    p.category,
    COUNT(*) AS total_orders,
    SUM(o.revenue) AS total_revenue,
    SUM(o.net_profit) AS total_net_profit,
    AVG(o.revenue) AS avg_order_value,
    ROUND(SAFE_DIVIDE(SUM(o.net_profit), SUM(o.revenue)) * 100, 2) AS avg_profit_margin,
    ROUND(SAFE_DIVIDE(SUM(o.is_returned), COUNT(*))*100, 4) AS return_rate
  FROM orders_clean o
  JOIN ecom.customers c ON o.customer_id = c.customer_id
  JOIN ecom.products p ON o.product_id = p.product_id
  GROUP BY c.city_tier, c.is_loyalty_member, p.category
),

abandon_summary AS (
  SELECT
    c.city_tier,
    c.is_loyalty_member,
    p.category,
    ROUND(SAFE_DIVIDE(
      SUM(CASE WHEN ce.purchased = 0 THEN 1 ELSE 0 END),
      COUNT(*)
    )*100, 4) AS cart_abandonment_rate
  FROM ecom.cart_events ce
  JOIN ecom.customers c ON ce.customer_id = c.customer_id
  JOIN ecom.products p ON ce.product_id = p.product_id
  GROUP BY c.city_tier, c.is_loyalty_member, p.category
)

SELECT
  r.city_tier,
  r.is_loyalty_member,
  r.category,
  r.total_orders,
  r.total_revenue,
  r.total_net_profit,
  r.avg_order_value,
  r.avg_profit_margin,
  r.return_rate,
  a.cart_abandonment_rate
FROM returns_summary r
LEFT JOIN abandon_summary a
  ON r.city_tier = a.city_tier
  AND r.is_loyalty_member = a.is_loyalty_member
  AND r.category = a.category
ORDER BY r.total_net_profit DESC;
