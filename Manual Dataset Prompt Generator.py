from csv import writer

topics = ["Self esteem","Relationships","Anger Management","Domestic Violence", "Substance Abuse","Family Conflict"]
emotions = ["Anger","Disgust","Fear","Happy","Sad","Surprised"]
intensity = ["Little(Low)","Kind of(Medium)","Extremely(High)"]    #Low, Medium, High

for genre in topics:
    for emt in emotions:
        for intense in intensity:
            message = "What are the 5 most common questions a person whose state currently is "+intense+" "+emt+" might ask a psychological counselor now on the topic of "+genre+" and what is a similar answer that can be given? Give the results in csv format as a table with the emotion("+emt+") followed by intensity("+intense+") then followed by the question then the answer, with it being separated by '|' instead of commas."
            list = [message,]
            with open('q&a.csv', mode='a') as f:
                writer_object = writer(f)
                writer_object.writerow(list)
                f.close()