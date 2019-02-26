import ROOT
import sys

c1 = ROOT.TCanvas( 'c1', 'Example with Formula', 200, 10, 700, 500 )

# Create a one dimensional function and draw it
fun1 = ROOT.TF1( 'fun1', 'abs(sin(x)/x)', 0, 10 )
c1.SetGrid()
fun1.Draw()
#c1.Update()

input("Press Enter to continue...")
