# Programming Assignment: Machine Problem 4: Hadoop MapReduce
## 1. Overview
Welcome to the Hadoop MapReduce programming assignment. You may choose to complete this machine problem in either Java or Python. Please select the language that you prefer. Before beginning this assignment, we recommend you practice the Tutorial: Docker installation and Tutorial: Introduction to Hadoop MapReduce.
## 2. General Requirements
Please note that our grader runs on a docker container and is NOT connected to the internet. Therefore, no additional libraries are allowed for this assignment. Also, you will NOT be allowed to create any file or folder outside the current folder (that is, you can only create files and folders in the folder that your solutions are in).
## 3. Sorting
When selecting the top N items in a list, sorting is necessary. Use the following steps to sort:

1. Sort the list ASCENDING based on Firstly value then Secondly on the key. If the key is a string, sort lexicographically.

2. Select the bottom N items in the sorted list as Top items.

## Python submission

**If you choose to do this assignment in Java, skip this part and go to the "Java submission" part above
##### Requirements

This assignment will be graded based on Python 3.6.
##### Procedures

Step 1: Run the provided Docker image (please follow "Tutorial: Docker installation").

Step 2: Download the project files.

Step 3: Change the current folder.

Step 4: Finish the exercises by editing the provided template files. You must complete the parts marked with TODO. Please note that you are NOT allowed to import any additional libraries.

Each exercise has one or more code templates. All you must do is edit these files.
Our autograder also uses the provided docker image.
For partial credit: Only submit the files related to the exercise in a zip format (MP4.zip). Example: For part A, only submit TitleCountMapper.py, TitleCountReducer.py, TopTitlesMapper.py, TopTitlesReducer.py files to receive a partial credit.

More information about these exercises is provided in the next section.

Step 5: After finishing the assignments, compress all your 14 python files (TitleCountMapper.py, TitleCountReducer.py, TopTitlesMapper.py, TopTitlesReducer.py, TopTitleStatisticsMapper.py, TopTitleStatisticsReducer.py, OrphanPagesMapper.py, OrphanPagesReducer.py, LinkCountMapper.py, LinkCountReducer.py, TopPolularLinksMapper.py, TopPolularLinksReducer.py, PopularityLeagueMapper.py, PopularityLeagueReducer.py) into "MP4.zip" and submit this zip file. 

Note: just like MP1, please do NOT put files into a folder and then compress this folder!!!

#### Exercise A: Top Titles

In this exercise, you will implement a counter for words in Wikipedia titles and an application to find the top words used in these titles. We have provided a template for this exercise in the following files:  TitleCountMapper.py, TitleCountReducer.py, TopTitlesMapper.py, TopTitlesReducer.py 

You must make the necessary changes to parts marked with TODO.

Your application takes a list of Wikipedia titles (one in each line) as an input and first tokenizes them using provided delimiters. After that, it makes the tokens lowercased, then removes common words from the provided stopwords. Next, your application selects the top 10 words, and finally, saves the count for them in the output. Use the method in section 3 Sorting to select top words.

First, you should tokenize Wikipedia titles, make the tokens lowercased, remove common words, and save the count for all words in the output with TitleCountMapper.py and TitleCountReducer.py.

You can test your output with:
```
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar -files TitleCountMapper.py,TitleCountReducer.py -mapper 'TitleCountMapper.py stopwords.txt delimiters.txt' -reducer 'TitleCountReducer.py' -input dataset/titles/ -output ./preA-output_Python
cat preA-output_Python/part-00000
```

The order of the output is NOT important. Here is a part of the output of this:

Because of the possible problems with special characters, we will not check the output for this part. We will only check the top words and their counts.

The following is the sample command we will use to run the application:
```
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar -files TitleCountMapper.py,TitleCountReducer.py -mapper 'TitleCountMapper.py stopwords.txt delimiters.txt' -reducer 'TitleCountReducer.py' -input dataset/titles/ -output ./preA-output_Python 
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar -files TopTitlesMapper.py,TopTitlesReducer.py -mapper 'TopTitlesMapper.py' -reducer 'TopTitlesReducer.py' -input ./preA-output_Python/ -output ./A-output_Python
```

If you want to check your output, run:
```
cat A-output_Python/part-00000
```

The order of lines matters. Also, make sure the key and value pairs in the final output are tab-separated.
#### Exercise B: Top Title Statistics

In this exercise, you will implement an application to find some statistics about the top words used in Wikipedia titles. We have provided a template for this exercise in the following files: TopTitleStatisticsMapper.py, TopTitleStatisticsReducer.py

You must make the necessary changes to parts marked with TODO.

Your output from Exercise A will be used here. The application saves the following statistics about the top words in the output: "Mean", "Sum", "Minimum" and "Maximum", and "Variance" of the counts. All values should be floored to be an integer. For the sake of simplicity, simply use Integer in all calculations.

The following is the sample command we will use to run the application:
```
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar -files TopTitleStatisticsMapper.py,TopTitleStatisticsReducer.py -mapper 'TopTitleStatisticsMapper.py' -reducer 'TopTitleStatisticsReducer.py' -input ./A-output_Python/ -output ./B-output_Python
```

If you want to check your output, run:
```
cat B-output_Python/part-00000
```

This formula calculates variance: Var(X)=E[(X−μ)^2]. Make sure the stats and the corresponding results are tab-separated.
#### Exercise C: Orphan Pages

In this exercise, you will implement an application to find orphan pages in Wikipedia. We have provided a template for this exercise in the following files: OrphanPagesMapper.py, OrphanPagesReducer.py

You must make the necessary changes to parts marked with TODO.

Your application takes a list of Wikipedia links (not Wikipedia titles anymore) as an input. All pages are represented by their ID numbers. Each line starts with a page ID, followed by a list of all the pages that the ID links to. The following is a sample line in the input:

In this sample, page 2 has links to pages 3, 747213, and so on. Note that links are not necessarily two-way. The application should save the IDs of orphan pages in the output. Orphan pages are pages to which no other pages link. Please sort the output in increasing order.

The following is the sample command we will use to run the application:
```
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar -files OrphanPagesMapper.py,OrphanPagesReducer.py -mapper 'OrphanPagesMapper.py' -reducer 'OrphanPagesReducer.py' -input dataset/links/ -output ./C-output_Python
```


If you want to check your output, run:
'''
cat C-output_Python/part-00000
'''

If you want to check a part of your output, run:
```
head C-output_Python/part-00000
```

The order of lines matters.
#### Exercise D: Top Popular Links

In this exercise, you will implement an application to find the most popular pages on Wikipedia. We have provided a template for this exercise in the following files: LinkCountMapper.py, LinkCountReducer.py, TopPopularLinksMapper.py, TopPopularLinksReducer.py

If you have finished Exercise A, LinkCountMapper.py, LinkCountReducer.py should produce output similar to TitleCountMapper.py, TitleCountReducer.py in Exercise A. Instead of printing the count for each title, LinkCountMapper.py and LinkCountReducer.py should output the link count for each page P or the number of pages linked to P. Be careful about the output format produced by LinkCountMapper.py and LinkCountReducer.py since their output is supposed to become the input of TopPopularLinksMapper.py. So if you use a tab to separate the page ID and its link count, your TitleCountMapper.py should also consume its input in this way.

All you need to do is make the necessary changes to parts that are marked with TODO.

Your application takes a list of Wikipedia links as input. All pages are represented by their ID numbers. Each line starts with a page ID,  followed by a list of all the pages the ID links to. The following is a sample line in the input:

In this sample, page 2 has links to pages 3, 747213, and so on. Note that links are not necessarily two-way. The application should save the IDs of the top 10 popular pages and the number of links to them in the output. A page is popular if more pages are linked to it. Use the method in section 3 Sorting to select top links.

The following is the sample command we will use to run the application:
```
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar -files LinkCountMapper.py,LinkCountReducer.py -mapper 'LinkCountMapper.py' -reducer 'LinkCountReducer.py' -input dataset/links/ -output ./linkCount-output_Python
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar -files TopPopularLinksMapper.py,TopPopularLinksReducer.py -mapper 'TopPopularLinksMapper.py' -reducer 'TopPopularLinksReducer.py' -input ./linkCount-output_Python -output ./D-output_Python
```

If you want to check your output, run:
```
cat D-output_Python/part-00000
```

The order of lines matters. Also, make sure the key and value pairs in the final output are tab-separated.
#### Exercise E: Popularity League

In this exercise, you will implement an application to calculate the rank of pages in a league using their popularity. Again, we have provided a template for this exercise in the following files:  PopularityLeagueMapper.py, PopularityLeagueReducer.py

You need to make the necessary changes to parts marked with TODO.

The popularity of a page is determined by the number of pages in the whole Wikipedia graph that link to that specific page. (Same number as Exercise D)

The input for this exercise will be the output from LinkCountReducer.py (linkCount-output_Python) from  Exercise D.

The application also takes a list of page IDs as an input (also called a league list). The goal of the application is to calculate the rank of pages in the league using their popularity.

A page's rank is the number of pages in the league with strictly less (not equal) popularity than the original page. Hint: pay careful attention to strictly less (not equal) part of the line when assigning ranks. Please sort based on the key in decreasing order.

The following is the sample command we use to run the application:
 ```
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar -files PopularityLeagueMapper.py,PopularityLeagueReducer.py -mapper 'PopularityLeagueMapper.py dataset/league.txt' -reducer 'PopularityLeagueReducer.py' -input ./linkCount-output_Python -output ./E-output_Python
```

If you want to check your output, run:
```
cat E-output_Python/part-00000
```

Note: if there are some pages not existing in the dataset, just ignore them in the output. Here is the output with League={88822,774931,4861926,1650573,66877,5115901,75323,4189215, 1}): (We ignore page #1, as it does not exist in the dataset.)

The order matters. Also, make sure the key and value pairs in the final output are tab-separated. 

Note that we will use a different League file in our test.
