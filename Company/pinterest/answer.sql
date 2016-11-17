/*      Write and save your SQL code in this file.
        Do not rename or move it.  */

SELECT A.name, M.title
FROM actor A, movie M
WHERE EXISTS ( 	SELECT *
				FROM  movie_actor MA 
				WHERE A.id = MA.actor_id AND M.id = MA.movie_id)