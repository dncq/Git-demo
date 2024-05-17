import matplotlib.pyplot as plt

# Data
categories = ['Non-quantized', 'Quantized']
scores = [0.2267, 0.2090]

# Plot
plt.bar(categories, scores, color=['blue', 'orange'])
plt.title('BLEU Score')
plt.ylabel('Score')
plt.ylim(0, 0.3)  # Adjust the y-axis limit if needed
plt.show()
