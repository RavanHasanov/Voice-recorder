from recorder import Recorder
r = Recorder()
r.record(10, output='out.wav')

Recorder.play('out.wav')

r.close()