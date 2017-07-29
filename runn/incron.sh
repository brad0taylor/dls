#!/bin/bash
echo "  " >> /home/brad/runn/incron.log
echo "Run incron job" >> /home/brad/runn/incron.log
echo "---------------------------------------------------"  >> /home/brad/runn/incron.log
home/brad/runn/run_incron.py >> /home/brad/runn/incron.log 2>> /home/brad/runn/incron.log
echo "---------------------------------------------------"  >> /home/brad/runn/incron.log
echo "done" >> /home/brad/runn/incron.log
echo "  "   >> /home/brad/runn/incron.log
