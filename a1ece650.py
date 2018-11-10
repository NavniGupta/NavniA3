import sys
import re
import ast

main_list = dict()
#function for checking street name is in valid format or not
def check_street(streetName):
    if all(a.isalpha() or a.isspace() for a in streetName ):
        return True
    else:
        return False
#function for checking if street to be changesd exits or not
def can_change(streetName):

    
        if streetName in main_list:
            return True
        else:

            return False
#function for checking parenthesis in input
def check_parenthesis(GPSlocation):
    s = []
    equal = True
    index = 0
    while index < len(GPSlocation) and equal:
        token = GPSlocation[index]
        if token == "(":
            s.append(token)
        elif token == ")":
            if len(s) == 0:
                equal = False
            else:
                s.pop()

        index += 1

    return equal and len(s) == 0

#function for checking valid format of coordinates
def is_vertex_valid(GPSlocation):
    regex = r'\(-?\d+,-?\d+\)'
    preg = re.compile(regex)
    result= preg.match(GPSlocation)
    return result   
   
#function for spiliting coordinate to get value of 'x' and 'y'    
'''def ast.literal_eval(pair):
    v1=re.split('\(|\)',pair)
    v1,w1=re.split(',',str(v1[1]))
    return v1,w1'''

#function for adding a street
def add_street(GPSlocation,streetName):
    
    
        if(check_parenthesis(GPSlocation)):
            GPSlocation1=re.sub(' +','',GPSlocation)
            GPSlocation1=re.sub('\)\(',') ( ',GPSlocation1)
            GPSlocation1=re.sub('\( ','(',GPSlocation1)
            GPSlocation1=GPSlocation1.split(' ')
            if all(is_vertex_valid(i) for i in GPSlocation1):
                 main_list[streetName] = GPSlocation1
            else:
                print "Error: enter vertices in a valid format."
        else:
             print "Error: Incorrect input format-unbalanced parenthesis"
    
#function for changing a street        
def change_street(GPSlocation,streetName):

        if(check_parenthesis(GPSlocation)):
            GPSlocation1=re.sub(' +','',GPSlocation)
            GPSlocation1=re.sub('\)\(',') ( ',GPSlocation1)
            GPSlocation1=re.sub('\( ','(',GPSlocation1)
            GPSlocation1=GPSlocation1.split(' ')
            if all(is_vertex_valid(i) for i in GPSlocation1):
                 main_list[streetName] = GPSlocation1
            else:
                print "Error: enter vertices in a valid format."
        else:
             print "Error: Incorrect input format-unbalanced parenthesis"

 #function for removing a street          
def remove_street(streetName):
      try:
                del main_list[streetName]
      except KeyError:
                sys.stderr.write("Error: " + streetName + "Street does not exist" + "\n")
                
def check_overlap(x,y,thislist,graph_points,graph_distinctVertices,graph_vertices,dictionary_intersectionPoints,vertices_intersection):  
                            new_vertex = "(" + str(x) + "," + str(y) + ")"
                            graph_points.extend(thislist)
                            dictionary_intersectionPoints.append(new_vertex)
                            vertices_intersection.append(thislist)
                            graph_points.append(new_vertex)
                            graph_distinctVertices = set(graph_points)
                            graph_points = list(graph_distinctVertices)
                            for z in range(0, len(graph_points)):
                                graph_vertices[z] = graph_points[z]
 #function for finding intersection between lines and finding vertex cover           
def graph_formation():
   
    list_of_vertices=list(main_list.values())
    vertices=list()
    graph_points=list()
    graph_distinctVertices=set()
    graph_vertices=dict()
    dictionary_intersectionPoints=list()
    vertices_intersection=list()
    y=list()
    q=1
    r=1
    #last_element=list()
    streets_count=len(list_of_vertices)
    vertices=[None]*streets_count
    #last_element=[None]*streets_count
    for o in range (0,streets_count):
        y=[i.split(', ', 1)[0] for i in list_of_vertices[o]]
        vertices[o]=y
    for i in range(0,streets_count):
        #print "hi"
        for j in range (i+1,streets_count):
             k=len(vertices[i])
             #print "hi"
             l=len(vertices[j])
             while q<k:
                 while r<l:
                      
                      p1=vertices[i][q-1]
                      p2=vertices[i][q]
                      p3=vertices[j][r-1]
                      p4=vertices[j][r]
                      
                      x1,y1 = ast.literal_eval(p1)
                      x2,y2 = ast.literal_eval(p2)
                      x3,y3 = ast.literal_eval(p3)
                      x4,y4 = ast.literal_eval(p4)
                      x1=float(x1);x2=float(x2); x3=float(x3);x4=float(x4);
                      y1=float(y1);y2=float(y2);y3=float(y3);y4=float(y4);
                      p1="(" + str(x1) + "," +str(y1) + ")"
                      p2="(" + str(x2) + "," +str(y2) + ")"
                      p3="(" + str(x3) + "," +str(y3) + ")"
                      p4="(" + str(x4) + "," +str(y4) + ")"
                      thislist = list((p1,p2,p3,p4))
                      A = x2 - x1    
                      B = y2 - y1
                      C = x4 - x3
                      D = y4 - y3
                      determinant = (-C * B + A * D)
                      min_x1 = min(x1, x2);min_x2 = min(x3, x4);max_x1 = max(x1, x2);max_x2 = max(x3, x4);
                      min_y1 = min(y1, y2);min_y2 = min(y3, y4);max_y1 = max(y1, y2);max_y2 = max(y3, y4);

                      if abs(determinant) < 1e-20: 
                          if(p1==p4):
                            check_overlap(x4,y4,thislist,graph_points,graph_distinctVertices,graph_vertices,dictionary_intersectionPoints,vertices_intersection)
                          elif(p2==p3):
                              check_overlap(x3,y3,thislist,graph_points,graph_distinctVertices,graph_vertices,dictionary_intersectionPoints,vertices_intersection)

                           
                    
                          elif(x1==x2==x3==x4):
                             y_range1=abs(y2-y1)
                             y_range2=abs(y4-y3)
                             if(y_range1 > y_range2):
                                big_line=1
                             elif(y_range2 > y_range1):
                                big_line=2
                             if(big_line == 1):
                                     if(y3>min_y1 and y3<max_y1):
                                         check_overlap(x3,y3,thislist,graph_points,graph_distinctVertices,graph_vertices,dictionary_intersectionPoints,vertices_intersection)

                                   
                                     if(y4>min_y1 and y4<max_y1):
                                         check_overlap(x4,y4,thislist,graph_points,graph_distinctVertices,graph_vertices,dictionary_intersectionPoints,vertices_intersection)

                                   
                            
                             if(big_line == 2):
                                if(y1>min_y2 and y1<max_y2):
                                    check_overlap(x1,y1,thislist,graph_points,graph_distinctVertices,graph_vertices,dictionary_intersectionPoints,vertices_intersection)

                                   
                                if(y2>min_y2 and y2<max_y2):
                                    check_overlap(x2,y2,thislist,graph_points,graph_distinctVertices,graph_vertices,dictionary_intersectionPoints,vertices_intersection)

                                    
                            
                          elif(y1==y2==y3==y4):
                             x_range1=abs(x2-x1)
                             x_range2=abs(x4-x3)
                             if(x_range1 > x_range2):
                                 big_line=1
                             elif(x_range2 > x_range1):
                                 big_line=2
                             if(big_line == 1):
                                if(x3>min_x1 and x3<max_x1):
                                    check_overlap(x3,y3,thislist,graph_points,graph_distinctVertices,graph_vertices,dictionary_intersectionPoints,vertices_intersection)

                                    
                                if(x4>min_x1 and x4<max_x1):
                                    check_overlap(x4,y4,thislist,graph_points,graph_distinctVertices,graph_vertices,dictionary_intersectionPoints,vertices_intersection)

                            
                             if(big_line == 2):
                                if(x1>min_x2 and x1<max_x2):
                                    check_overlap(x1,y1,thislist,graph_points,graph_distinctVertices,graph_vertices,dictionary_intersectionPoints,vertices_intersection)

                                    
                                if(x2>min_x2 and x2<max_x2):
                                    check_overlap(x2,y2,thislist,graph_points,graph_distinctVertices,graph_vertices,dictionary_intersectionPoints,vertices_intersection)

                                    
                            
                                
         
                      else:
                         s = (-B * (x1 - x3) + A * (y1 - y3)) / determinant
                         t = ( C * (y1 - y3) - D * (x1 - x3)) / determinant

                         if (bool(s >= 0) & bool(s <= 1) & bool(t >= 0) & bool(t <= 1)):
                             X=x1 + (t * A)
                             Y=y1 + (t * B)

                             X = float("{0:.2f}".format(X))
                             Y = float("{0:.2f}".format(Y))
                             new_vertex="(" + str(X) + "," +str(Y) + ")"                            
                             graph_points.extend(thislist)
                             dictionary_intersectionPoints.append(new_vertex)
                             vertices_intersection.append(thislist)
                             graph_points.append(new_vertex)
                             graph_distinctVertices=set(graph_points)
                             graph_points=list(graph_distinctVertices)
                             for z in range(0,len(graph_points)):
                                 graph_vertices[z]=graph_points[z]
                         else: 
                             pass
                         
                      r=r+1
                 q=q+1
                 r=1
             q=1
                                 
    sys.stdout.write( "V ")
    sys.stderr.write("V ")
    sys.stdout.flush()
    sys.stdout.write(str(len(graph_vertices))+'\n')
    sys.stderr.write(str(len(graph_vertices))+'\n')
    sys.stdout.flush()         
   

    graph_GPSedges=list() 
    graph_GPSedgeset=set()
    repetitive_edges=list()
    repetitive_edges1=list()
    for t in range(0, len(dictionary_intersectionPoints)):
        intersection_pt=dictionary_intersectionPoints[t]
        vertexlist=vertices_intersection[t]
        [p1, p2, p3, p4]=vertexlist
        
        edge_intersection = graph_vertices.keys()[graph_vertices.values().index(intersection_pt)]
        edge_p1 = graph_vertices.keys()[graph_vertices.values().index(p1)]
        edge_p2 = graph_vertices.keys()[graph_vertices.values().index(p2)]
        edge_p3 = graph_vertices.keys()[graph_vertices.values().index(p3)]
        edge_p4 = graph_vertices.keys()[graph_vertices.values().index(p4)]
        
        edge1="<"+str(edge_intersection) + "," + str(edge_p1) + ">"
                
        edge2="<"+str(edge_intersection) + "," + str(edge_p2) + ">"
               
        edge3="<"+str(edge_intersection) + "," + str(edge_p3) + ">"
                
        edge4="<"+str(edge_intersection) + "," + str(edge_p4) + ">"
                    
        edgelist = list((edge1,edge2,edge3,edge4))
        graph_GPSedges.extend(edgelist)
        graph_GPSedgeset=set(graph_GPSedges)
        graph_GPSedges=list(graph_GPSedgeset)
        distinct_x=list()

    '''  for g in graph_vertices:
            
            if intersection_pt == graph_vertices[g]:
                edge_intersection=g
        for key,val in graph_vertices.items():
            if val==p1:
                edge_p1=key
                
        for key,val in graph_vertices.items():
            if val==p2:
                edge_p2=key
                
        for key,val in graph_vertices.items():
                 if val==p3:
                     edge_p3=key
                                                          
        for key,val in graph_vertices.items():
                if val==p4:
                    edge_p4=key  '''
                   
    
                    
                    
    '''  for n in range(0,len(graph_GPSedges)):
        pair=graph_GPSedges[n]
        pair=re.sub('<','(',pair)
        pair=re.sub('>',')',pair)
        y,z=ast.literal_eval(pair)
        if(y==z):
            del_check="<" + str(y) + "," + str(z) + ">"
            repetitive_edges.append(del_check)
        
        distinct_x.append(y)
        distinct_set=set(distinct_x)
        distinct_x=list(distinct_set)
        for n1 in range(0, len(distinct_x)):
            for n2 in range(n1+1,len(distinct_x)):
                edge_betweeen = "<" + str(distinct_x[n1]) + "," + str(distinct_x[n2]) + ">"
                graph_GPSedges.append(edge_betweeen)
                graph_GPSedgeset = set(graph_GPSedges)
                graph_GPSedges = list(graph_GPSedgeset)'''


    for b in range(0,len(graph_GPSedges)):
        edge = graph_GPSedges[b]
        edge = re.sub('<', '(', edge)
        edge = re.sub('>', ')', edge)
        pair1,pair2 = ast.literal_eval(edge)
        #pair1,pair2=int(pair1),int(pair2)
        if(pair1==pair2):
            del_check="<" + str(pair1) + "," + str(pair2) + ">"
            repetitive_edges.append(del_check)

        for c in graph_vertices:
            vertex1=graph_vertices[pair1]

            vertex2=graph_vertices[pair2]

            
            v_x1,v_y1=ast.literal_eval(vertex1)
            v_x2,v_y2=ast.literal_eval(vertex2)
            
            #y,z=ast.literal_eval(pair)
            min_x1 = min(v_x1, v_x2)
            max_x1 = max(v_x1, v_x2)
            min_y1 = min(v_y1, v_y2)
            max_y1 = max(v_y1, v_y2)
            pair_check=graph_vertices[c]

            check_x,check_y=ast.literal_eval(pair_check)
            if((bool(check_x!=min_x1) & bool( check_x !=max_x1)) | ((bool(check_y!=min_y1) & bool(check_y!=max_y1)))):
                if(bool(check_x <= max_x1) & bool(check_x >= min_x1)):
                    if(bool(check_y <= max_y1) & bool(check_y >= min_y1)):
                        del_check="<" + str(pair1) + "," + str(pair2) + ">"

                        repetitive_edges.append(del_check)
                        repetitive_edges_set=set(repetitive_edges)
                        repetitive_edges=list(repetitive_edges_set)


    for k in range(0,len(repetitive_edges)):
        graph_GPSedges.remove(repetitive_edges[k])
    
    for g in range(0,len(graph_GPSedges)):
        for g1 in range(g+1,len(graph_GPSedges)):
            edge_new1 = graph_GPSedges[g]
            edge_new1 = re.sub('<', '(', edge_new1)
            edge_new1 = re.sub('>', ')', edge_new1)
            pair1,pair2 = ast.literal_eval(edge_new1)
            edge_new2 = graph_GPSedges[g1]
            edge_new2 = re.sub('<', '(', edge_new2)
            edge_new2 = re.sub('>', ')', edge_new2)
            pair3,pair4 = ast.literal_eval(edge_new2)
            if(pair1==pair4 and pair2==pair3):
                delete="<" + str(pair1) + "," + str(pair2) + ">"
                repetitive_edges1.append(delete)
                repetitive_edges_set1=set(repetitive_edges1)
                repetitive_edges1=list(repetitive_edges_set1)

    for n1 in range(0,len(repetitive_edges1)):
        graph_GPSedges.remove(repetitive_edges1[n1])
    
    for d in range(0, len(graph_GPSedges)):
        pair = graph_GPSedges[d]
        pair = re.sub('<', '(', pair)
        pair = re.sub('>', ')', pair)
        x_coord, y_coord = ast.literal_eval(pair)
        distinct_x.append(x_coord)
        distinct_set = set(distinct_x)
        distinct_x = list(distinct_set)
        #print distinct_new_vertices
        for e in range(0, len(distinct_x)):
            for f in range(e+1,len(distinct_x)):
                edge_between = "<" + str(distinct_x[e]) + "," + str(distinct_x[f]) + ">"
                graph_GPSedges.append(edge_between)
                    
                graph_set = set(graph_GPSedges)
                graph_GPSedges = list(graph_set)
                

    sys.stdout.write("E {")
    sys.stderr.write("E {")
    sys.stdout.flush()
    count=len(graph_GPSedges)
    for u in graph_GPSedges:
        sys.stdout.flush()
        sys.stdout.write(u)
        sys.stderr.write(u)
        sys.stdout.flush()
        count=count-1
        if(count):
            sys.stdout.write(',')
            sys.stderr.write(',')
            sys.stdout.flush()
    sys.stdout.write("}" + '\n')
    sys.stderr.write("}" + '\n')
    sys.stdout.flush()
    
    
    
    

def main():
    
    while True:
        #coordinates=sys.stdin.readline()
        #coordinates=coordinates.replace('\n','')
        
        coordinates=raw_input()
        if(coordinates ==''):
            break
        elif(coordinates[0]=='r'):
            y=re.split(' +"|"|',coordinates)
        else:
            y=re.split('" +| +"',coordinates)
        if(len(y)==1):
            command=y[0]
        elif(len(y)==2):
            command=y[0]
            streetName=y[1]
            streetName=streetName.lower()   
        elif(len(y)==3):
            command=y[0]
            streetName=y[1]
            streetName=streetName.lower()
            GPSlocation=y[2]
        else:
            sys.stdout.write("Error: " + "Wrong selection of command")
            continue
        if command == 'a':
            try:
                check_change=can_change(streetName)
                check=check_street(streetName)
                if check==True:
                    if check_change==False:
                        add_street(GPSlocation,streetName)
                    else:
                        print "Error: Street currently exists."
                else:
                    print "Error: Enter street in valid format."
            except UnboundLocalError:
                 sys.stderr.write("Error: " + "Please enter correct input" + "\n")
                 
            
        elif command == 'c':
            try:
                check_change=can_change(streetName)
            
                if check_change==True:
                
                    change_street(GPSlocation,streetName)
              
                else:
                    print"Error: 'c' or 'r' specified for a street that does not exist."
            except UnboundLocalError:
                 sys.stderr.write("Error: " + "Please enter correct input" + "\n")
                 
        elif command == 'r':
            try:
                remove_street(streetName)
            except UnboundLocalError:
                 sys.stderr.write("Error: " + "Please enter correct input" + "\n")    
            
        elif command == 'g':
            graph_formation()
          
        else:
            print 'Error: ' + 'Invalid command.Press a,g or r for valid commands.'

if __name__ == '__main__':
    main()