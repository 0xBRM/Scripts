import vapoursynth as vs
import sys
from fractions import Fraction

core = vs.get_core(threads=5)

# vspipe --y4m 1080p.vpy - | ffmpeg -i pipe: encoded.mkv -c:v libx264 -preset placebo -crf 10 -x264-params keyint=123:min-keyint=20 -c:a copy output.mkv

core.std.LoadPlugin('/usr/lib/libffms2.so')
core.std.LoadPlugin ('/usr/local/lib/libfmtconv.so')
core.std.LoadPlugin('/usr/local/lib/libf3kdb.so')

clip = video_in
# applies deband
clip = core.f3kdb.Deband(clip, grainy=0, grainc=0, range=12, output_depth=16)
# downscales to 1920x1080 using spline36, play around with chroma ss values
clip = core.fmtc.resample(clip, 853, 480, css='444', kernel='spline36')

clip.set_output()
