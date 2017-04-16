import vapoursynth as vs
import sys

core = vs.get_core(threads=5)

# vspipe --y4m 1080p.vpy - | ffmpeg -i pipe: encoded.mkv -c:v libx264 -preset placebo -crf 10 -x264-params keyint=123:min-keyint=20 -c:a copy output.mkv

core.std.LoadPlugin('/usr/lib/libffms2.so')
core.std.LoadPlugin('/usr/local/lib/libf3kdb.so')


clip = video_in
# applies deband
clip = core.f3kdb.Deband(clip, grainy=0, grainc=0, range=12, output_depth=16)

clip.set_output()
