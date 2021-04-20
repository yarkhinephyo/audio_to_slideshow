from moviepy.editor import VideoFileClip, AudioFileClip

def save_output_video(gif, audio, save_path):

    clip1 = VideoFileClip(gif)
    clip2 = AudioFileClip(audio)

    final_clip = clip1.set_audio(clip2)
    final_clip.write_videofile(save_path)
    