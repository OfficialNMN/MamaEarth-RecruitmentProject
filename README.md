# MamaEarth-RecruitmentProject

## About Files
1. MamaEarthProductClassifier.csv   ----> file that contains the ProductName, Category and Ingredients.
2. MamaEarthProductClassifier.ipynb ----> jupyter notebook that contains the trained NaiveBayes Classification model.
3. ProductClassifier.py             ----> python script to scrape MamaEarthProductClassifier.csv from the website.
4. MamaEarthScrape.csv              ----> file that contains ProductName ,ProductLink, PackSize, Price, Reviews, Ratings, Discounts.
5. MamaEarthScrape.py               ----> python scrpit to scrape MamaEarthScrape.csv from the website.

## About Classifier Model
A Classification NaiveBayes model is trained which can fetch the key ingredient used in the product and also classify the product based on its category. For this the site is again scraped and has columns - ProductName, Category and Ingredient. First the dataset is loaded using Pandas library and preprocessing is done and the dataset is then splitted into train and test data using sklearn inbuilt modules. Now, A Pipeline using NaiveBayes Algorithm and other text preprocessing techniques using NLTK is created and trained on the training dataset saved in a .csv file. The model trained is now evaluated using performance metrics on the test data. A sample input is given to the trained model to see what output it predicts.
