SELECT COUNT(*)
FROM "flights-db"."mp9"
WHERE month = 12 
AND day = 25 
AND origin_airport = 'ORD' 
AND scheduled_departure >= 800
AND scheduled_departure < 1200;