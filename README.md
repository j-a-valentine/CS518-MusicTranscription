# CS518-MusicTranscription

## Installation

Before you begin, ensure you have **Python** and **FFmpeg** installed on your system.

### Installing FFmpeg

To install FFmpeg, follow the instructions specific to your operating system:

- **Windows**: You can download the FFmpeg executable from the [official website](https://ffmpeg.org/download.html) and follow the installation instructions provided.
- **macOS**: You can install FFmpeg using [Homebrew](https://brew.sh/). Open your terminal and run the following command: ```brew install ffmpeg```


### Installing Python Dependencies

We recommend using a virtual environment to manage your project dependencies. If you haven't already, you can create one using the following commands:

```
# Create a virtual environment
python -m venv venv ```

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS and Linux
source venv/bin/activate

Once your virtual environment is activated, you can install the required Python packages using pip:
pip install -r requirements.txt

### Setting Up and Running the Program

To run the program smoothly, follow these simple steps:

1. **Create a `.env` file**: Create a file named `.env` in the root directory of the project. Add the following line to the `.env` file:
```OPENAI_API_KEY=YOUR_OPENAI_API_KEY```
Replace `YOUR_OPENAI_API_KEY` with your actual OpenAI API key. If you don't have one, sign up for an account on the [OpenAI website](https://openai.com/) to obtain your API key.

2. **Create a folder titled `audio`**: In the root directory of the project, create a folder named `audio`.

3. **Add .mp3 Files**: Place any `.mp3` files you want to use with the program in the `audio` folder. Make sure each `.mp3` file is named after the title of the song. These files will be used by the program for processing. For example, if you have a song titled "Firework" name the corresponding `.mp3` file as `firework.mp3`.

4. **Run the Program**:
    - Run the program using the following command:
      ```
      python main.py "SONG_TITLE"
      ```
      Replace `"SONG_TITLE"` with the title of the song you want to process, without the `.mp3` extension.
    - Optionally, you can specify the `pipeline` parameter to run the program in pipeline mode:
      ```
      python main.py "SONG_TITLE" pipeline
      ```
      Running in pipeline mode will use the most recent transcription as the prediction.

5. **Important Note**: If you want to regenerate the predictions using AI, delete the `.json` file of the corresponding song. Make sure to delete the entire `.json` file and not just its contents. This will prompt the program to reprocess the song and generate fresh predictions.




