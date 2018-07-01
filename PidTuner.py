import numpy as np 
#import casadi as ca
import julia

class PidTuner:

	def __init__(self, modelFitter, dt):
		# get order, then call .predict() with 2 args
		self.modelFitter = modelFitter
		j=julia.Julia()
		pid=j.include("PID_Optimizer")

	# Objective fct: Depends on unknown y-states, known reference
	def getObjective(self, states, ref):
		obj = 0.
	def getConstraints(self, states, pid_params):
		# Consistency constraint on states
		# u_k = PID(e_k, e_k-1, itg(.), Kp, Kd, Ki)
		# y_k = f(u_k.., y_k-1..)
		print("empty")

	def fitPid(self):
		### Inputs
		#Kontinuierliche Matrizen A,B,C,D 
		#maximales überschwingen
		#endzeit tf
		#anzahl der disk punkte
		#unterer bound für u
		#oberer bound für u
		### Outputs
		# x[0] -status ob program optimal gelöst wurde
		# x[1] [P,I,D] Parameter
		# x[2] Output y
		# x[3] Timevector t
		x=self.pid(A,B,C,D,SollWert,max_overshoot,tf,Number_Of_Disc_Points,u_lower_bound,u_upper_bound)
		PID=x[1]
		print("P=" PID[0])
		print("I=" PID[1])
		print("D=" PID[2])


