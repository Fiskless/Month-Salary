# Programming vacancies compare

This project allow us to get data from from job search sites such as HeadHunter and Superjob by using it API (API HeadHunter - https://dev.hh.ru/, API SuperJob - https://api.superjob.ru/. Through this project we can compare the vacancies which we are interested in. As a result we get two tables which have 3 columns: "Vacancies found" where number of vacancies found is presented, average salary in column "Average salary" calculated for vacancies which are in column "Vacancies processed". These data presented for multiple programming languages which are shown in column "Programming language"

### How to install

For API HeadHunter you don't need secret key.

For API SuperJob you need one. In order to get it you should register application by following this link: https://api.superjob.ru/register/. You can use any data, nobody will check it. After registrate your appliction data will be as shown below. We are interested in "Secret key" in chapter "Access options". The example of "Secret key" is in file example.end in directory of this project. 
 ````
Application options

Application Name	JobJob
App Description	123qwe
Application site	https://www.anysite.com
Callback URL	
The contact person	JobMaster
Email the address	example@mail.ru
Website	https://www.anysite.com

Access options

ID	9999
Secret key	'Your secret key for API SuperJob'

````

The result of this project is shown below:

`````
$python main.py

+SuperJob Moscow-------+-----------------+---------------------+----------------+
| Programming language | Vacancies found | Vacancies processed | Average salary |
+----------------------+-----------------+---------------------+----------------+
| Javascript           | 84              | 45                  |         102370 |
| Java                 | 84              | 45                  |         102370 |
| Python               | 35              | 13                  |         102566 |
| Ruby                 | 4               | 2                   |         153500 |
| PHP                  | 68              | 45                  |         118653 |
| Scala                | 3               | 1                   |         184500 |
| C                    | 21              | 18                  |          71152 |
| Shell                | 2               | 1                   |         200000 |
+----------------------+-----------------+---------------------+----------------+
+HeadHunter Moscow-----+-----------------+---------------------+----------------+
| Programming language | Vacancies found | Vacancies processed | Average salary |
+----------------------+-----------------+---------------------+----------------+
| Javascript           | 2841            | 787                 |         144867 |
| Java                 | 2842            | 786                 |         144903 |
| Python               | 1783            | 421                 |         163161 |
| Ruby                 | 208             | 67                  |         160228 |
| PHP                  | 1276            | 625                 |         134859 |
| Scala                | 203             | 44                  |         188189 |
| C                    | 7283            | 988                 |         140053 |
| Shell                | 144             | 30                  |         161636 |
+----------------------+-----------------+---------------------+----------------+
`````

### Project Goals
The code is written for educational purposes on online-course for web-developers dvmn.org.
