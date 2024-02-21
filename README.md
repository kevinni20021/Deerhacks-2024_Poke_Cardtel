# Poke Cardtel
# About
Created for Deerhacks 2023, this projects grades pokemon cards using the PSA standard using convolutional neural networks. Our goal is to help people get into the world of pokemon card trading and allow people to easily understand the rarity and price of their cards. This project was created by David Hu, Kai Wang, Kevin Ni, and Weiming Quan.

# How it works
## Data Collection
Using the selenium python library, we scraped over 40000 images off the PSA websites and grouped them into 6 categories: PSA10, PSA9, PSA8, PSA7, PSA6, Low Grade. Low grade cards are all cards on the PSA website rated 5 or below, and the rest of the categories are respective to the grade they were given on the website.

## Preproccessing
The preprocssing step was done via the opencv library. We removed all background noise by using a filter and cropping out just the card itself using computer vision techniques. For images that cannot be preprocessed (ie too much noise or no card), we will remove them from the dataset at this point. 

## Machine learning
Using the preprocessed dataset, we used tensorflow and the VGG16 architecture ot train our model. First we loaded the pretrained weights from imagenet for object recognition. Then using transfer learning techniques, we froze the base layer and trained the top model for our dataset. Then we unfroze the entire model and trained the entire network with our dataset. Ultimately, we achieved 90% accuracy with our test set.

# Pricing
Given the name and grade of the card, we will scrape a website using selenium and find out how much the card is worth.

## Application
Utilizng react-native and flask, we built a responsive frontend and backend that will use the model to predict the the quality and price of a given card. First the user will take a picture of both the front and the back of a card, then we will preprocess the card using the tool we described earlier. After the preprocessing step, we will run the image data through the model and predict what grade the card could be. We then ask the user to input the name of the card and return the price of the card given the grade.

# Requirments
- python
- tensorflow
- selenium
- opencv
- flask
- numpy
- javascript
- react-native

