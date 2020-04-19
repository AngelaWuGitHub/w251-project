# w251-project

## What is this project about
The ability to use deep learning networks for sign language recognition has gained considerable attention over the past few years. There have been considerable advancements in using both 2D and 3D data representing letters, words and actions of the sign language to their written language translation. 
We implement an approach of training video data to achieve a considerable accuracy on inferring words when deployed on a Jetson TX2. 

## Data
The dataset used in the project was the ASLLVD (American sign language lexicon video dataset) present here: 
http://csr.bu.edu/asl/asllvd/annotate/index.html
All raw data required to execute the below steps is present in AWS S3 at
https://s3.console.aws.amazon.com/s3/buckets/w251-project/data/raw/?region=us-west-1

## Steps to execute
The diagram below lists out the steps required in training the model on an ibmcloud instance. All scripts required for execution are in "ibmcloud" folder.
The scripts assume the following structure on AWS:  
w251-project  
|_____data  
        |_____raw  
        |_____processed    
                        |______json  
                        |______videos  



### Preprocessing

### Inference on Jetson TX2

## Conclusion
