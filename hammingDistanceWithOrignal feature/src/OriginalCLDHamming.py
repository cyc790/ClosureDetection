#!/usr/bin/env python
# coding=utf-8
import time
import matplotlib.pylab as plt
import OriginalCalHamming
import OriginalPlotPresicionRecall




if __name__=='__main__':
    
    Start=time.clock()
    Recall=[]
    Precision=[]
    titles=[]
    lines=[]
    
#--------------------------------------------------------------------------------------------------------------------------------------    
    
    
#     conv3Hamming=OriginalCalHamming.HammingDistance('conv3')
#     conv3Hamming.LoadOriginFeature()
#     start=time.clock()
#     conv3Hamming.CalHammingDistance()
#     end=time.clock()
#     print "Caculate hamming distance is (%f)s!"  %(end-start)
#     conv3Hamming.WriteHammingDistance()
# 
    conv3Plot=OriginalPlotPresicionRecall.PlotPrecisionRecall('conv3',64896,40)
    conv3Plot.LoadHammingDistance()
    conv3Plot.FindMaxAndMinDistance()
    conv3Plot.PlotPrecisionRecall()
    Recall.append(conv3Plot.recall)
    Precision.append(conv3Plot.precision)
    titles.append(conv3Plot.layerName)
 
# 
# #--------------------------------------------------------------------------------------------------------------------------------------    
#     
#     
#     conv3Hamming=OriginalCalHamming.HammingDistance('conv4')
#     conv3Hamming.LoadOriginFeature()
#     start=time.clock()
#     conv3Hamming.CalHammingDistance()
#     end=time.clock()
#     print "Caculate hamming distance is (%f)s!"  %(end-start)
#     conv3Hamming.WriteHammingDistance()
# 
    conv3Plot=OriginalPlotPresicionRecall.PlotPrecisionRecall('conv4',64896,40)
    conv3Plot.LoadHammingDistance()
    conv3Plot.FindMaxAndMinDistance()
    conv3Plot.PlotPrecisionRecall()
    Recall.append(conv3Plot.recall)
    Precision.append(conv3Plot.precision)
    titles.append(conv3Plot.layerName)
# 
# 
# #--------------------------------------------------------------------------------------------------------------------------------------    
#     
#     
#     conv3Hamming=OriginalCalHamming.HammingDistance('conv5')
#     conv3Hamming.LoadOriginFeature()
#     start=time.clock()
#     conv3Hamming.CalHammingDistance()
#     end=time.clock()
#     print "Caculate hamming distance is (%f)s!"  %(end-start)
#     conv3Hamming.WriteHammingDistance()
# 
    conv3Plot=OriginalPlotPresicionRecall.PlotPrecisionRecall('conv5',43264,40)
    conv3Plot.LoadHammingDistance()
    conv3Plot.FindMaxAndMinDistance()
    conv3Plot.PlotPrecisionRecall()
    Recall.append(conv3Plot.recall)
    Precision.append(conv3Plot.precision)
    titles.append(conv3Plot.layerName)
# 
# #--------------------------------------------------------------------------------------------------------------------------------------    
# 
# 
#     conv3Hamming=OriginalCalHamming.HammingDistance('pool5')
#     conv3Hamming.LoadOriginFeature()
#     start=time.clock()
#     conv3Hamming.CalHammingDistance()
#     end=time.clock()
#     print "Caculate hamming distance is (%f)s!"  %(end-start)
#     conv3Hamming.WriteHammingDistance()
 
    conv3Plot=OriginalPlotPresicionRecall.PlotPrecisionRecall('pool5',9216,40)
    conv3Plot.LoadHammingDistance()
    conv3Plot.FindMaxAndMinDistance()
    conv3Plot.PlotPrecisionRecall()
    Recall.append(conv3Plot.recall)
    Precision.append(conv3Plot.precision)
    titles.append(conv3Plot.layerName)
     
#     
# #--------------------------------------------------------------------------------------------------------------------------------------    
# 
#      
#     conv3Hamming=OriginalCalHamming.HammingDistance('fc6')
#     conv3Hamming.LoadOriginFeature()
#     start=time.clock()
#     conv3Hamming.CalHammingDistance()
#     end=time.clock()
#     print "Caculate hamming distance is (%f)s!"  %(end-start)
#     conv3Hamming.WriteHammingDistance()
#     
    conv3Plot=OriginalPlotPresicionRecall.PlotPrecisionRecall('fc6',4096,40)
    conv3Plot.LoadHammingDistance()
    conv3Plot.FindMaxAndMinDistance()
    conv3Plot.PlotPrecisionRecall()
    Recall.append(conv3Plot.recall)
    Precision.append(conv3Plot.precision)
    titles.append(conv3Plot.layerName)
# 
# #--------------------------------------------------------------------------------------------------------------------------------------    
# 
#  
#     conv3Hamming=OriginalCalHamming.HammingDistance('fc7')
#     conv3Hamming.LoadOriginFeature()
#     start=time.clock()
#     conv3Hamming.CalHammingDistance()
#     end=time.clock()
#     print "Caculate hamming distance is (%f)s!"  %(end-start)
#     conv3Hamming.WriteHammingDistance()
#     
    conv3Plot=OriginalPlotPresicionRecall.PlotPrecisionRecall('fc7',4096,40)
    conv3Plot.LoadHammingDistance()
    conv3Plot.FindMaxAndMinDistance()
    conv3Plot.PlotPrecisionRecall()
    Recall.append(conv3Plot.recall)
    Precision.append(conv3Plot.precision)
    titles.append(conv3Plot.layerName)
# 
# 
# #--------------------------------------------------------------------------------------------------------------------------------------    
# 
#  
#     conv3Hamming=OriginalCalHamming.HammingDistance('fc8')
#     conv3Hamming.LoadOriginFeature()
#     start=time.clock()
#     conv3Hamming.CalHammingDistance()
#     end=time.clock()
#     print "Caculate hamming distance is (%f)s!"  %(end-start)
#     conv3Hamming.WriteHammingDistance()
    
    conv3Plot=OriginalPlotPresicionRecall.PlotPrecisionRecall('fc8',205,40)
    conv3Plot.LoadHammingDistance()
    conv3Plot.FindMaxAndMinDistance()
    conv3Plot.PlotPrecisionRecall()
    Recall.append(conv3Plot.recall)
    Precision.append(conv3Plot.precision)
    titles.append(conv3Plot.layerName)
    

#--------------------------------------------------------------------------------------------------------------------------------------    

    plt.figure(0)
    plt.title("Precision_Recall")  
    plt.xlabel("recall")
    plt.ylabel("precision")
    plt.xlim(0,100)
    plt.ylim(0,100)
    i=0
    for x in Recall:
        line,=plt.plot(Recall[i],Precision[i]) 
        lines.append(line)
        i=i+1
    plt.legend(lines,titles,loc='lower left')    
    plt.savefig('../plot/Orignal_Precision_Recall_L='+str(conv3Plot.L)+'.eps')
    
    End=time.clock()
    print "The TOTAL TIME is (%f)s!"  %(End-Start)
