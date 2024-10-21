# Overview #

## Background Context ##
Before undertaking this project, I thought I knew SQL very well. Well, that's why it's a good idea not to thing too highly of yourself, because there' always something to learn, no matter where you are at.

Covered in this project are various advanced MYSQL Concepts which include:
- How to optimize queries by adding indexes;
- Implementing stored procedures and functions;
- Implementing views; and
- Implementing trigers
- And picked up along the way:
  - Cursors
  - Compound statements, etc.

## Reference Materials ##
The following can be used for referencing these areas, curated for optimized understanding:
- [MySQL cheatsheet](https://devhints.io/mysql)
- [MySQL Performance: How To Leverage MySQL Database Indexing](https://www.liquidweb.com/blog/mysql-optimization-how-to-leverage-mysql-database-indexing/)
- [Stored Procedure](https://www.w3resource.com/mysql/mysql-procedure.php)
- [Triggers](https://www.w3resource.com/mysql/mysql-triggers.php)
- [Views](https://www.w3resource.com/mysql/mysql-views.php)
- [Functions and Operators](https://dev.mysql.com/doc/refman/5.7/en/functions.html)
- [Trigger Syntax and Examples](https://dev.mysql.com/doc/refman/5.7/en/trigger-syntax.html)
- [CREATE TABLE Statement](https://dev.mysql.com/doc/refman/5.7/en/create-table.html)
- [CREATE PROCEDURE and CREATE FUNCTION Statements](https://dev.mysql.com/doc/refman/5.7/en/create-procedure.html)
- [CREATE INDEX Statement](https://dev.mysql.com/doc/refman/5.7/en/create-index.html)
- [CREATE VIEW Statement](https://dev.mysql.com/doc/refman/5.7/en/create-view.html)
- [Calculating Weighted-Average](https://www.wikihow.com/Calculate-Weighted-Average)

<hr />

## Folder Details ###
- **Date Created:** Thur 17 Oct 2024
- **Author:** [William Inyam](https.//github.com/thecypherzen/alx-backend-storage/0x00-MySQL_Advanced).
- **Project Timeline:**
- **Released:** Wed Oct 16 2024 - 6am.
  - **1st Deadline** Fri Oct 18 2024 - 6am.
  - **Duration:** 48hrs
  - **Completed:** Mon 21 Oct 2024 - 7:05am.



## Files  ###
- *This is a high-level view of files in this directory and a short description of what they contain. Each file is task based and a full description of each task, requirement and constraints can be found in each file. The tasks are designed to test understanding of these concepts above....* **enjoy!**

| **SN** | File                         | Description                                         |
|----|------------------------------|-----------------------------------------------------|
| 1. | [0-uniq_users.sql](https://github.com/thecypherzen/alx-backend-storage/blob/main/0x00-MySQL_Advanced/0-uniq_users.sql) | A script that creates a table `users`. |
| 2. | [1-country_users.sql](https://github.com/thecypherzen/alx-backend-storage/blob/main/0x00-MySQL_Advanced/1-country_users.sql) | A script that creates a table `users` with and added column that uses `ENUM`. Details in file. |
| 3. | [2-fans.sql](https://github.com/thecypherzen/alx-backend-storage/blob/main/0x00-MySQL_Advanced/2-fans.sql) | A script that that ranks country origins of bands, ordered by the number of (non-unique) fans. Details in file. |
| 4. | [3-glam_rock.sql](https://github.com/thecypherzen/alx-backend-storage/blob/main/0x00-MySQL_Advanced/3-glam_rock.sql) | A script that lists all bands with Glam rock as their main style, ranked by their longevity. Details in file. |
| 5. | [4-store.sql](https://github.com/thecypherzen/alx-backend-storage/blob/main/0x00-MySQL_Advanced/4-store.sql) | A script that creates a trigger that decreases the quantity of an item after adding a new order. Details in file. |
| 6. | [5-valid_email.sql](https://github.com/thecypherzen/alx-backend-storage/blob/main/0x00-MySQL_Advanced/5-valid_email.sql) | A script that creates a trigger that resets the attribute valid_email only when the email has been changed. Details in file. |
| 7. | [6-bonus.sql](https://github.com/thecypherzen/alx-backend-storage/blob/main/0x00-MySQL_Advanced/6-bonus.sql) | A script that creates a stored procedure `AddBonus` that adds a new correction for a student. Details in file. |
| 8. | [7-average_score.sql](https://github.com/thecypherzen/alx-backend-storage/blob/main/0x00-MySQL_Advanced/7-average_score.sql) | A script that creates a stored procedure `ComputeAverageScoreForUser` that computes and store the average score for a student. Note: An average score can be a decimal. Details in file. |
| 9. | [8-index_my_names.sql](https://github.com/thecypherzen/alx-backend-storage/blob/main/0x00-MySQL_Advanced/8-index_my_names.sql) | A script that creates an index `idx_name_first` on the table `names` and the first letter of `name`. Details in file. |
| 10. | [9-index_name_score.sql](https://github.com/thecypherzen/alx-backend-storage/blob/main/0x00-MySQL_Advanced/9-index_name_score.sql) | A script that creates an index `idx_name_first_score` on the table `names` and the first letter of `name` and the `score`. Details in file. |
| 11. | [10-div.sql](https://github.com/thecypherzen/alx-backend-storage/blob/main/0x00-MySQL_Advanced/10-div.sql) | A script that creates a function `SafeDiv` that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0. Details in file. |
| 12. | [11-need_meeting.sql](https://github.com/thecypherzen/alx-backend-storage/blob/main/0x00-MySQL_Advanced/11-need_meeting.sql) | A script that creates a view `need_meeting` that lists all students that have a score under 80 (strict) and no `last_meeting` or more than 1 month. Details in file. |
| 13. | [100-average_weighted_score.sql](https://github.com/thecypherzen/alx-backend-storage/blob/main/0x00-MySQL_Advanced/100-average_weighted_score.sql) | A script that create stored procedure `ComputeAverageWeightedScoreForUser` that computes and stores the average weighted score for a student. Details in file. |
| 14. | [101-average_weighted_score.sql](https://github.com/thecypherzen/alx-backend-storage/blob/main/0x00-MySQL_Advanced/101-average_weighted_score.sql) | A script that creates a stored procedure `ComputeAverageWeightedScoreForUsers` that computes and store the average weighted score for all students. Details in file. |
