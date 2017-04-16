import vapoursynth as vs
import edi_rpow2 as edi
import sys

core = vs.get_core(threads=5)

# vspipe --y4m 1080p.vpy - | ffmpeg -i pipe: encoded.mkv -c:v libx264 -preset placebo -crf 10 -x264-params keyint=123:min-keyint=20 -c:a copy output.mkv

core.std.LoadPlugin('/usr/lib/libffms2.so')
core.std.LoadPlugin ('/usr/local/lib/libfmtconv.so')
core.std.LoadPlugin('/usr/local/lib/libf3kdb.so')
core.std.LoadPlugin('/usr/local/lib/libnnedi3.so')


clip = video_in
# applies deband
clip = core.f3kdb.Deband(clip, preset=nograin, range=12, output_depth=16)
# doubles with NNEDI3, 1280x720 --> 2560x1440
clip = core.fmtc.bitdepth(clip=clip,bits=16)
clip = edi.nnedi3_rpow2(clip=clip,rfactor=2,correct_shift='fmtconv',nsize=0,nns=4,qual=2,etype=0,pscrn=3,opt=True)
# downscales to 1920x1080 using spline36 
clip = core.fmtc.resample(clip, 1920, 1080, css='444', kernel='spline36')

clip.set_output()
