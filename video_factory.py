from moviepy.editor import TextClip, CompositeVideoClip

def render_video(script):

    clip = TextClip(
    script,
    fontsize=40,
    size=(1080,1920),
    method="caption"
    )

    video = CompositeVideoClip([clip])

    file = "videos/video.mp4"

    video.write_videofile(file, fps=24)

    return file
