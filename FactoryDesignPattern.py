"""
https://youtu.be/s_4ZrtQs8Do?si=HRXGBvO0KHjMB2Rx

This video explains factory design in the easiest way with a clear example. See the video.
I will try to recreate the example here. 

The concept of factory design pattern is to hide creation from use. So, it hides the creation of objects 
from where it is used. Let's try an example. It's gonna be a long example. I will try the example 
used in the linked video. 
"""

from abc import ABC, abstractmethod

# Let say we want to export audio and video. We will create different exporter of different format. But we
# want each of the exporter to have two method, one for processing and one to export. 
# So let's start with creating Abstract classes first 
class VideoExporter(ABC):
    @abstractmethod
    def process_video(self):
        """Processes a Video"""
        pass

    @abstractmethod
    def export_video(self):
        """Exports the Video"""
        pass

class AudioExporter(ABC):
    @abstractmethod
    def process_audio(self):
        """Processes a Audio"""
        pass

    @abstractmethod
    def export_audio(self):
        """Exports the Audio"""
        pass

# Now let's implement our exporters

class LowQualityVideoExporter(VideoExporter):
    def process_video(self):
        print(f"Processing Low Qualitiy video")
    def export_video(self):
        print(f"Exporting Low quality video")

class HighQualityVideoExporter(VideoExporter):
    def process_video(self):
        print(f"Processing High Qualitiy video")
    def export_video(self):
        print(f"Exporting High quality video")

class MasterQualityVideoExporter(VideoExporter):
    def process_video(self):
        print(f"Processing Master Qualitiy video")
    def export_video(self):
        print(f"Exporting Master quality video")

class LowQualityAudioExporter(AudioExporter):
    def process_audio(self):
        print(f"Processing Low Qualitiy audio")
    def export_audio(self):
        print(f"Exporting low quality audio")

class HighQualityAudioExporter(AudioExporter):
    def process_audio(self):
        print(f"Processing High Qualitiy audio")
    def export_audio(self):
        print(f"Exporting High quality audio")

class MasterQualityAudioExporter(AudioExporter):
    def process_audio(self):
        print(f"Processing Master Qualitiy audio")
    def export_audio(self):
        print(f"Exporting Master quality audio")

# Now we have created three different types of audio and video exporter based on the quality.
# Now we want to take input from the user what kinds of exporter they want and do that export for them.
# Let's create a main function that will do the job

def main():
    quality = input(f"Please enter your desired quality(Low, High, Master) for export: ")
    quality = quality.lower()

    if quality == "low":
        audio_exporter = LowQualityAudioExporter()
        video_exporter = LowQualityVideoExporter()
    if quality == "high":
        audio_exporter = HighQualityAudioExporter()
        video_exporter = HighQualityVideoExporter()
    elif quality == "master":
        audio_exporter = MasterQualityAudioExporter()
        video_exporter = MasterQualityVideoExporter()
         
    
    audio_exporter.process_audio()
    video_exporter.process_video()
    audio_exporter.export_audio()
    video_exporter.export_video()


main()

# output:
    # Please enter your desired quality(Low, High, Master) for export: Low
    # Processing Low Qualitiy audio
    # Processing Low Qualitiy video
    # Exporting audio quality audio
    # Exporting Low quality video

# The output is ok, it's working alright. 
# Now if wee look at the main() function, we can see that the objects are created where they are used.
# The main() has so many responsiblities here. With factory, we can reduce responsibility from a single function. 
# We can create the objects in a different function and use them in the main(). we can create a factory function 
# that will give us the object for us, and in main() we will only use the objects. Also, to avoid these many
# class call, we can create Exporter class that will export both audio and video.

print(f"\n")
print("#"*50)
print(f"\n")

class Exporter(ABC):
    @abstractmethod
    def get_audio_exporter():
        pass

    @abstractmethod
    def get_video_exporter():
        pass

class LowQualityExporter(Exporter):
    def get_audio_exporter(self):
        return LowQualityAudioExporter()
    def get_video_exporter(self):
        return LowQualityVideoExporter()

class HighQualityExporter(Exporter):
    def get_audio_exporter(self):
        return HighQualityAudioExporter()
    def get_video_exporter(self):
        return HighQualityVideoExporter()
class MasterQualityExporter(Exporter):
    def get_audio_exporter(self):
        return MasterQualityAudioExporter()
    def get_video_exporter(self):
        return MasterQualityVideoExporter()

def get_exporter():
    quality = input(f"Please enter your desired quality(Low, High, Master) for export: ")
    quality = quality.lower()

    if quality == "low":
        return LowQualityExporter()
    elif quality == "high":
        return HighQualityExporter()
    elif quality == 'master':
        return MasterQualityExporter()
    
def main_with_factory():
    exporter = get_exporter()

    audio_exporter = exporter.get_audio_exporter()
    video_exporter = exporter.get_video_exporter()

    audio_exporter.process_audio()
    video_exporter.process_video()

    audio_exporter.export_audio()
    video_exporter.export_video()

main_with_factory()

# output
    # Please enter your desired quality(Low, High, Master) for export: Low
    # Processing Low Qualitiy audio
    # Processing Low Qualitiy video
    # Exporting low quality audio
    # Exporting Low quality video

"""
We can see, we have the same output!! So, it worked. Now what all the fuss is about?! 
We had to write three extra class and an extra function to do the same task! So what's the excitment is about?

Look at the main_with_factory() function now. It's clean and concise now. It doesn't have all the responsibilities now.
Imagine the part where we need to export the audio and video. With previous implementation, we had so many responsibilites
to hande to export the video and audio. Now it's simple and less responsibility. We can now just import the get_exporter()
function and call the exporters. We don't need to worry about the creation of exporter objects. 
Exactly that's what Factory design pattern does!
"""
