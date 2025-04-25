# **Markov Chain Text Generator 🧠🔀**

Welcome to the **Markov Chain Text Generator**! This tool allows you to upload text files and generate new, random text based on the word patterns of the uploaded content. It's based on the **Markov Chain** algorithm, which predicts the next word based on previous words, creating a "chain" of random but meaningful words.

---

## **✨ Features**
- **Upload multiple text files**: Upload one or more `.txt` files to generate new text.
- **Markov Chain Text Generation**: Generates random text based on word patterns found in the uploaded files.
- **Customizable**: You can modify the graph logic or text generation process if you want to build something even more advanced.
- **Instant Feedback**: Get instant feedback and errors if the file is not in the correct format or if something goes wrong.

---

## **🚀 How to Use**

### Step 1: **Upload Text Files**
- Use the **Upload** button to upload one or more text files.
- Supported file type: `.txt`.

### Step 2: **Text Processing**
- Once you upload a file, the app will extract words, remove punctuation, and process the text into a format that can be used to generate new content.

### Step 3: **Generate Text**
- Click on the **Generate Text** button to see new, random text generated based on the words from the uploaded files.

### Step 4: **Output the Text**
- After processing, the app will show the generated text below the button. Enjoy your new Markov Chain generated text! ✨

---

## **⚙️ How It Works**

1. **Text Extraction**: The uploaded files are read, and words are extracted. Punctuation and special characters are removed.
2. **Graph Construction**: A graph is built using the words from the file. Each word becomes a vertex, and edges are added based on the word sequence.
3. **Markov Chain Generation**: Using the graph, the app generates text by predicting the next word based on previous words.

---

## **📝 Example**

Here’s an example of how the app works:

1. **Upload** a file with content like:

