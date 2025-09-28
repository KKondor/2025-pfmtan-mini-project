-- Stored Procedure: get_joke_by_id
CREATE DEFINER=`root`@`%` PROCEDURE `get_joke_by_id`(IN joke_id INT)
BEGIN
SELECT idx, joke_text, rating
FROM jokes
WHERE idx = joke_id;
END;

---

-- Stored Procedure: get_jokes_list
CREATE DEFINER=`root`@`%` PROCEDURE `get_jokes_list`(
IN sort_order VARCHAR(10),   -- lehet: 'asc', 'desc', 'rating'
IN filter_type VARCHAR(20)   -- lehet: 'all', 'informatics', 'animal', 'weather', 'mom', 'dad', 'school', 'pun'
)
BEGIN
-- ha nincs szűrés (all), akkor minden típus jöhet
IF filter_type = 'all' THEN
IF sort_order = 'asc' THEN
SELECT idx, joke_text, rating
FROM jokes
ORDER BY joke_text ASC;
ELSEIF sort_order = 'desc' THEN
SELECT idx, joke_text, rating
FROM jokes
ORDER BY joke_text DESC;
ELSEIF sort_order = 'rating' THEN
SELECT idx, joke_text, rating
FROM jokes
ORDER BY rating DESC;
END IF;
ELSE
IF sort_order = 'asc' THEN
SELECT idx, joke_text, rating
FROM jokes
WHERE joke_type = filter_type
ORDER BY joke_text ASC;
ELSEIF sort_order = 'desc' THEN
SELECT idx, joke_text, rating
FROM jokes
WHERE joke_type = filter_type
ORDER BY joke_text DESC;
ELSEIF sort_order = 'rating' THEN
SELECT idx, joke_text, rating
FROM jokes
WHERE joke_type = filter_type
ORDER BY rating DESC;
END IF;
END IF;
END;

---

-- Stored Procedure: update_joke_rating
CREATE DEFINER=`root`@`%` PROCEDURE `update_joke_rating`(
IN joke_idx INT,
IN operation VARCHAR(10)  -- 'add' vagy 'subtract'
)
BEGIN
IF operation = 'add' THEN
UPDATE jokes
SET rating = rating + 1
WHERE idx = joke_idx;
ELSEIF operation = 'subtract' THEN
UPDATE jokes
SET rating = rating - 1
WHERE idx = joke_idx;
END IF;
END;