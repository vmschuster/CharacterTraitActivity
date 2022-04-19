# Word Cloud Sorter
This script was used to sort the output of a google doc where each member of
 my varsity team wrote down positive character traits for one of their
  teammates. It then sorted them into individual csv files for each teammate
   with the number of times each word was used, in order to input into [this
    wordcloud generator.](https://www.wordclouds.com)
    
It also outputs a csv file titled "All" with all of the traits used to
 describe every member of the team and the corresponding frequency. 

 
 # Format of Input
 Input file should be called "traits.csv" and be in the following format
 
__File Name__ : traits.csv
 
| Timestamp (ignored)| Author's Name (ignored)|Teammates Name | Trait 1 | Trait 2| Trait 3| Trait 4| Trait 5|
|:----------|:-------------:|------:|---:|----:|----:|----:|----:|
| 3/25/2021 11:08:49 | Jenna | Emily | Kind | Driven | Smart | Gritty | Empathetic |


# Format of Output

Consider a teammate named Emily:

__File Name__: Emily.csv

| Frequency of Word | Word | Colour |
|:------|-------|------|
| 1 | Friendly | #8793dd | 

