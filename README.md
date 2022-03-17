# State Election Analysis

## Overview of Project
A state election audit analysis was performed to gather various statistical information (such as the total vote count, count by county, and the distribution of votes across candidates) relating to the current election across three counties of Jefferson, Denver, and Arapahoe.

### Purpose
The goal of the current election analysis was to assist the election comission in examining the trends within the voting preferences of citizens in the three counties of Jefferson, Denver, and Arapahoe. Specifically, the code created for the analysis collected data such as the total vote count, the vote count distribution by county (both in absolute units and in percentages), and the vote count by candidate (in absolute units and in percentages, as well). The code also determined the most active county (based on the by-county turnout), as well as the election winner.

## Election-Audit Results
![Screenshot_2](https://user-images.githubusercontent.com/99566803/158908913-8c5af629-c6b7-4091-aa92-2e4c3b2eb614.png)

The results of the python-enabled analysis are provided below.
* The total vote count across all three examined counties amounted to **396,711** votes.

* The county distrubition was, as follows:

  * The county of **Jefferson** accounted for **38,855** votes, which represents approximately **10.5%** of all votes casted.

  * The county of **Denver** accounted for **306,055** votes, which represents approximately **82.8%** of all votes casted.

  * The county of **Arapahoe** accounted for **24,801** votes, which represents approximately **6.7%** of all votes casted.

* As a result, the county that held the **largest** vote was **Denver**.

* The candidate distribution was, as follows:

  * **Clarles Casper Stockham** received **85,213** votes, which accounted for **23.0%** of all votes casted.

  * **Diana DeGette** received **272,892** votes, which accounted for **73.8%** of all votes casted.

  * **Raymon Anthony Doane** received **11,606** votes, which accounted for **3.1%** of all votes casted.

* Consequently, **Diana DeGette** was found to be the winner of the election, with **272,892** votes, or **73.8%** of the votes, being cast in her favour.

## Election-Audit Summary

**Current Code's Outside Applicability:**

As mentioned previously, the Python script created for the current analysis is capable of counting the total vote count, as well as the vote count specific to a particular county or candidate, and is capable of determining the "owner" of the highest score in each respective category (i.e., most actively voting county or the most popular electorate candidate). Current script, however, can be easily modified and used for any other elections, as long as the election data is (or can be) stored in an CSV file type. The code is modular, and can be modified, or extended, to analyze other categories of interest that might be deemed beneficial in an electoral analysis (e.g., the code can be catered to calculate the percentage of population that voted in a particular county, or to determine the most prominent politican alignment of voters within a specified county).
