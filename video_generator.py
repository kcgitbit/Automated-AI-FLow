from moviepy.editor import TextClip, CompositeVideoClip

def generate_video(script):

    txt_clip = TextClip(script, fontsize=50)

    video = CompositeVideoClip([txt_clip])

    video.write_videofile("video.mp4", fps=24)

    return "video.mp4"
