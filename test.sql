INSERT INTO stores_products (id_product, id_store) VALUES (%s, %S) FROM (
    SELECT product.id, store.id FROM Product INNER JOIN Store ON Product.store = Store.name 
    WHERE Product.store IS NOT NULL) 
-- );

SELECT product.id as product, store.id as store FROM Product INNER JOIN Store ON Product.store = Store.name WHERE Product.store IS NOT NULL;

