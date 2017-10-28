#------------------------------------------------------------------------------
# connect_pool2.py (Section 2.2 and 2.4)
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Copyright 2017, Oracle and/or its affiliates. All rights reserved.
#------------------------------------------------------------------------------

import cx_Oracle
import threading

pool = cx_Oracle.SessionPool("pythonhol", "welcome", "localhost/orclpdb",
                             min = 2, max = 5, increment = 1, threaded = True)

def Query():
    con = pool.acquire()
    cur = con.cursor()
    for i in range(4):
        cur.execute("select myseq.nextval from dual")
        seqval, = cur.fetchone()
        print("Thread", threading.current_thread().name, "fetched sequence =", seqval)

numberOfThreads = 2
threadArray = []

for i in range(numberOfThreads):
    thread = threading.Thread(name = '#' + str(i), target = Query)
    threadArray.append(thread)
    thread.start()

for t in threadArray:
    t.join()

print("All done!")