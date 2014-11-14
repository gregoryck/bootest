from boopak.package import bimport
from boodle import agent
import random

water = bimport('org.boodler.old.water')
motor = bimport('org.boodler.old.motor')
thunder = bimport('org.boodler.sample.thunder')
noise = bimport('com.goob.noise')
hardhat = bimport('com.eblong.zarf.hardhat')


class Example(agent.Agent):
    def run(self):
        # self.sched_note(water.water_rushing, 1, 0.5)
        # self.sched_note(water.droplet_plink, delay=4.8)

        pitch = random.uniform(0.4, 0.5)
        level = random.uniform(1.8, 2.2)
        self.sched_note(thunder.distant_low_2, pitch, level)
        pitch = random.uniform(0.03, 0.08)
        level = random.uniform(0.8, 1.2)
        delay = random.uniform(0.1, 2)
        # dur = self.sched_note(noise.white, pitch, level)
        # print dur

        
        # self.sched_note(hardhat.MotorRun, pitch, level)
        self.sched_note(motor.whine_run, pitch, level)

        self.resched(delay)

