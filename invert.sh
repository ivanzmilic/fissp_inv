#!/bin/bash
echo "Running a simple inversion according to the invert_hinode file..."
pkill imaster
sleep 1.0
/home/milic/codes/snapi/master/imaster -v &
echo "Master process running... "
sleep 0.5
/home/milic/codes/snapi/slave/islave &
echo "Worker process running..."
sleep 0.5
/home/milic/codes/snapi/jsub/jsub -v -cfg invert_hinode.cfg
echo "Job submitted! Everything should be running now."
echo "Check the progress with tail -f invlog.000001."
echo "Once the calculation is finished, you can ../jsub/jub another job, or pkill imaster."