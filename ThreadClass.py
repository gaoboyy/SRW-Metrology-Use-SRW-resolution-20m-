import threading


class ThreadClass(threading.Thread):
    def run(self,v,op):
        srwl_bl.SRWLBeamline(_name=v.name, _mag_approx=mag).calc_all(v, op)
