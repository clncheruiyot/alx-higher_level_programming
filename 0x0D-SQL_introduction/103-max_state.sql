-- displays max temperature of each state ordered by the State name.

SELECT state, MAX(value) as max_temp FROM temperatures GROUP BY state ORDER BY state;;
