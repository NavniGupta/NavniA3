#include <unistd.h>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <cstdlib>
#include <string>

using namespace std;
namespace patch
{
    template < typename T > std::string to_string( const T& n )
    {
        std::ostringstream stm ;
        stm << n ;
        return stm.str() ;
    }
}



unsigned int NumberOfStreets ( unsigned int k )
{

    std::ifstream urandom("/dev/urandom");


    if (urandom.fail()) {
        std::cerr << "Error: cannot open /dev/urandom\n";
        return 1;
    }
    unsigned int rand = 3;
    urandom.read((char*)&rand, sizeof(unsigned int));
    rand = rand % (k-2+1) +2;
    urandom.close();
    return (unsigned int) rand;

}

unsigned int NumberOfLineSeg (unsigned int k)
{

    std::ifstream urandom("/dev/urandom");


    if (urandom.fail()) {
        std::cerr << "Error: cannot open /dev/urandom\n";
        return 1;
    }
    unsigned int rand = 3;
    urandom.read((char*)&rand, sizeof(unsigned int));
    rand = rand % (k-1+1) + 1;
    urandom.close();
    return (unsigned int) rand;


}

unsigned int WaitTime (unsigned int k)
{

    std::ifstream urandom("/dev/urandom");


    if (urandom.fail()) {
        std::cerr << "Error: cannot open /dev/urandom\n";
        return 1;
    }
    unsigned int time = 3;
    urandom.read((char*)&time, sizeof(unsigned int));
    time = time % (k-5+1) + 5;
    urandom.close();
    return (unsigned int) time;


}

int coordinate_value (unsigned int k)
{

    std::ifstream urandom("/dev/urandom");


    if (urandom.fail()) {
        std::cerr << "Error: cannot open /dev/urandom\n";
        return 1;
    }
    unsigned int rand = 3;
    urandom.read((char*)&rand, sizeof(int));
    rand = rand % (k+k);
    int out= rand - k ;
    urandom.close();
    return out;


}

void StreetName( vector<string> &street , unsigned int NumberOfStreets)
{
    string name = "a";
    for (unsigned int i=0; i < NumberOfStreets; i++)
    {
        street.push_back(name);
        name = name +'a';
    }

}

int MaxOfXY( int a1, int a2)
{

    int max1;
    if ( a1 > a2)
    {
        max1 = a1;
        return max1;
    }
    max1 = a2;
    return max1;

}

int MinOfXY( int a1, int a2)
{

    int min1;
    if ( a1 > a2)
    {
        min1 = a2;
        return min1;
    }

    min1 = a1;
    return min1;

}



bool Check_Intersect( int x1, int y1, int x2, int y2, int x3, int y3, int x4, int y4)
{
    double xnum, xden, xcoor, ynum, yden, ycoor;

    xnum = ((x1*y2-y1*x2)*(x3-x4) - (x1-x2)*(x3*y4-y3*x4));
    xden = ((x1-x2)*(y3-y4) - (y1-y2)*(x3-x4));
    xcoor =  xnum / xden;

    ynum = (x1*y2 - y1*x2)*(y3-y4) - (y1-y2)*(x3*y4-y3*x4);
    yden = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4);
    ycoor = ynum / yden;

    int min_x1, min_x2, max_x1, max_x2, min_y1, min_y2, max_y1, max_y2;

    min_x1 = MinOfXY(x1,x2);
    max_x1 = MaxOfXY(x1,x2);
    min_x2 = MinOfXY(x3,x4);
    max_x2 = MaxOfXY(x3,x4);
    min_y1 = MinOfXY(y1,y2);
    max_y1 = MaxOfXY(y1,y2);
    min_y2 = MinOfXY(y3,y4);
    max_y2 = MaxOfXY(y3,y4);

    if ( min_x1<= xcoor &&  xcoor <= max_x1)
        if ( min_x2 <= xcoor && xcoor <= max_x2)
            if ( min_y1 <= ycoor && ycoor <= max_y1)
                if ( min_y2 <= ycoor && ycoor <= max_y2)
                    return true;
    return false;

}



bool CheckPoint ( vector<int> coordinate, int x, int y)
{
    int s = coordinate.size();
    if ( coordinate.empty())
    {

        return true;
    }if ( s == 2)
    {
        if (( x == coordinate[0]) && (y == coordinate[1]) )
        {

            return false;
        }

        return true;
    }
    else
    {
        //check duplicate coordinates
        for (int i = 0; i < coordinate.size(); i = i + 2){
            if (x == coordinate[i] && y == coordinate[i+1]){
                return false;
            }
        }

        double k1, k2;
        //{0,10,0,10,4,4,5,5,6,6,5,7,0,0,7,7}
        if ( x == coordinate[s-2] && x == coordinate[s-4])
            return false;

        //check intersection
        if ( (x == coordinate[s-2]) && (x != coordinate[s-4]))
        {
            if ( s == 4)
                return true;
            else
            {
                for ( int i = s-3; i >=2; i = i-2 )
                {
                    if ( Check_Intersect(x,y,coordinate[s-2],coordinate[s-1],coordinate[i-1],coordinate[i],coordinate[i-3],coordinate[i-2]))
                        return false;

                }

                return true;
            }
        }

        if ( (coordinate[s-4] == coordinate[s-2]) && (x != coordinate[s-2]))
        {
            if ( s == 4)
                return true;
            else
            {
                for ( int i = s-3; i >=0; i = i-2 )
                {
                    if ( Check_Intersect(x,y,coordinate[s-2],coordinate[s-1],coordinate[i-1],coordinate[i],coordinate[i-3],coordinate[i-2]))
                        return false;

                }

                return true;
            }
        }

        //check in a line

        k1 = ((y - coordinate[s-1]) / (x-coordinate[s-2]));
        k2 = ((coordinate[s-1]) - coordinate[s-3]) / (coordinate[s-2]-coordinate[s-4]);

        if (k1 == k2)
            return false;

        else
        {

            if ( s == 4)
                return true;
            else
            {
                for ( int i = s-3; i >=0; i = i-2 )
                {
                    if ( Check_Intersect(x,y,coordinate[s-2],coordinate[s-1],coordinate[i-1],coordinate[i],coordinate[i-3],coordinate[i-2]))
                        return false;

                }

                return true;
            }

        }


    }

}





int main (int argc, char **argv) {

    std::string svalue, nvalue, lvalue, cvalue;
    unsigned int S_intVal = 10, N_intVal = 5, L_intVal = 5, C_intVal = 20;
    int c;
    int k;
    int s_num, l_num, x_cord, y_cord;
    unsigned int w_sed;

    vector<string> Namestreet;
    vector<int> street_line_num;
    vector<int> coordinate;

    opterr = 0;


    while ((c = getopt(argc, argv, "s:n:l:c:")) != -1) {
        switch (c) {
            case 's':
                svalue = optarg;
                S_intVal = std::atoi(svalue.c_str());
                if (S_intVal < 2)
                {
                    cerr << "Error: the number is too small (after s)"<<endl;
                    exit(1);
                }

                break;
            case 'n':
                nvalue = optarg;
                N_intVal = std::atoi(nvalue.c_str());
                if (N_intVal < 1)
                {
                    cerr << "Error: the number is too small (after n)"<<endl;
                    exit(1);
                }

                break;
            case 'l':
                lvalue = optarg;
                L_intVal = std::atoi(lvalue.c_str());
                if (L_intVal < 5)
                {
                    cerr << "Error: the number is too small (after l)"<<endl;
                    exit(1);
                }

                break;
            case 'c':
                cvalue = optarg;
                C_intVal = std::atoi(cvalue.c_str());
                if (C_intVal < 1)
                {
                    cerr << "Error: the number is too small (after c)"<<endl;
                    exit(1);
                }

                break;

            case '?':
                if (optopt == 's') {
                    std::cerr << "Error: option -" << optopt
                              << " requires an argument." << std::endl;
                    break;
                }
                else if (optopt == 'n') {
                    std::cerr << "Error: option -" << optopt
                              << " requires an argument." << std::endl;
                    break;
                }
                else if (optopt == 'l') {
                    std::cerr << "Error: option -" << optopt
                              << " requires an argument." << std::endl;
                    break;
                }
                else if (optopt == 'c') {
                    std::cerr << "Error: option -" << optopt
                              << " requires an argument." << std::endl;
                    break;
                }

                else
                    std::cerr << "Error: unknown option: " << optopt << std::endl;
                    break;

        }


    }

    while (true)
    {




        {
            for(std::vector<string>::iterator it = Namestreet.begin(); it != Namestreet.end(); it++)
            {
                cout<<"r "<<'"'<<*it<<'"'<<endl;

            }

            Namestreet.clear();
            street_line_num.clear();

        }


        s_num = NumberOfStreets(S_intVal);

        StreetName(Namestreet, s_num);


        for (int j = 0; j < s_num; j++)
        {
            l_num = NumberOfLineSeg(N_intVal);
            street_line_num.push_back(l_num);

        }

        int index = 0;

        for (int mk = 0; mk < street_line_num.size(); mk++)
        {
            coordinate.clear();     //save coordinates of each street
            int times = 0;
            int error = 0;
            while ( times < street_line_num[mk]+1 )
            {
                x_cord = coordinate_value(C_intVal);
                y_cord = coordinate_value(C_intVal);
                if (CheckPoint(coordinate, x_cord, y_cord))
                {
                    coordinate.push_back(x_cord);
                    coordinate.push_back(y_cord);
                    times++;
                    error = 0;
                }

                else
                {

                    if ( error == 25)
                    {
                        cerr<<"Error: failed to generate valid input for 25 simultaneous attempts"<<endl;
                        exit(1);   // ? how to exit
                    }

                    error++;
                }


            }



            string a_output;
            a_output = string("a \"") + Namestreet[index] + "\" ";


            for (int mk = 0; mk < coordinate.size(); mk = mk+2)
            {
                string a,b;
                if (coordinate[mk]<0){
                  a = "-"+patch::to_string(coordinate[mk]*(-1));
                } else {
                  a = patch::to_string(coordinate[mk]);
                }
                if (coordinate[mk+1]<0){
                  b = "-"+patch::to_string(coordinate[mk+1]*(-1));
                } else {
                  b = patch::to_string(coordinate[mk+1]);
                }
                a_output = a_output + '('+ a + ','+ b +')';
            }

            cout<<a_output<<endl;

            index++;
        }

        // g command
            cout<<'g'<<endl;
            w_sed = WaitTime(L_intVal);
            usleep(w_sed*1000000);

        }

return 0;
}










