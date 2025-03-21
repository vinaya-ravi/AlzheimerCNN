# Alzheimer's Disease Classification using Deep Learning

**Overview**<br>
This project implements a **Convolutional Neural Network (CNN)** to classify Alzheimer's Disease into four stages:<br>
- **Non-Demented**<br>
- **Very Mild Demented**<br>
- **Mild Demented**<br>
- **Moderate Demented**<br>
The model analyzes medical images to provide accurate classification, aiding in early diagnosis and treatment planning. The dataset is sourced from open-access repositories, ensuring diversity and reliability.

**System Design**<br>
The classification system follows a structured pipeline:<br>
- **Dataset Preparation**: Images labeled into four classes.<br>
- **Preprocessing**: Includes normalization, resizing, and dataset splitting (80% training, 20% testing).<br>
- **Feature Extraction**: CNN extracts features such as edges and textures indicative of Alzheimer's Disease.<br>
- **Model Training**: CNN is trained using backpropagation and gradient descent to minimize errors.<br>
- **Validation & Testing**: Evaluated on unseen data to ensure generalization.<br>
- **Result Analysis**: Metrics like accuracy, precision, recall, and confusion matrix are computed.

**System Architecture**<br>
The CNN architecture includes:<br>
- **Input Layer**: Processes preprocessed image data.<br>
- **Hidden Layers**: Convolutional layers for feature extraction, pooling layers for dimensionality reduction, and fully connected layers for classification.<br>
- **Output Layer**: Softmax activation to predict class probabilities.

**Data Flow**<br>
Input raw dataset → Preprocessing (normalization & scaling) → Train/Test Split<br>
Training Data → CNN Training → Model Validation → Performance Evaluation<br>
Testing Data → Model Testing → Classification Results

**Results**<br>
The model achieves the following performance metrics:<br>
- **Accuracy**: High classification accuracy across all four classes.<br>
- **Precision & Recall**: Reliable predictions with minimal false positives/negatives.<br>
- **Confusion Matrix**: Highlights correct classifications and areas for improvement.

**Key Insights**<br>
- The CNN effectively identifies patterns in medical images relevant to Alzheimer's Disease stages.<br>
- Performance can be further enhanced through advanced architectures like ResNet or EfficientNet.<br>
- The model demonstrates strong generalization capabilities on unseen data.

**Conclusion**<br>
This deep learning-based approach provides an efficient solution for Alzheimer's Disease classification, with potential applications in medical diagnostics. Future work may include deploying the model as a web application or integrating it with clinical workflows for real-time analysis.
