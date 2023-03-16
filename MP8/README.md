# MP8 SparkSQL Template

This is the Java and Python template for MP8 SparkSQL.

# Note for M1 Mac 

If you're using M1 Mac, you will need to modify the Dockerfile before building it by changing `/usr/lib/jvm/java-1.8.0-openjdk-amd64` to `/usr/lib/jvm/java-1.8.0-openjdk-arm64`

## Log 

Last updated in Feb 2022, by Yifan Chen (yifanc3@illinois.edu).

Updated in April 2021, by Ruiyang Chen (rc5@illinois.edu).

## Sample Output of 'MP8\_SQLite.py'
~~~sh
Opened database successfully
Table created successfully
ID =  1
NAME =  Paul
ADDRESS =  California
SALARY =  20000.0 

ID =  2
NAME =  Allen
ADDRESS =  Texas
SALARY =  15000.0 

ID =  3
NAME =  Teddy
ADDRESS =  Norway
SALARY =  20000.0 

ID =  4
NAME =  Mark
ADDRESS =  Rich-Mond 
SALARY =  65000.0 

Records created successfully
Total number of rows updated : 5
Total number of rows deleted : 6
~~~
