import math

def make_translate( x, y, z ):
    m = new_matrix()
    ident(m)
    m[0][3] = x
    m[1][3] = y
    m[2][3] = z
    return m

def make_scale( x, y, z ):
    m = new_matrix()
    ident(m)
    m[0][0] = x
    m[1][1] = y
    m[2][2] = z
    return m

def make_rotX( theta ):
    rad=math.radians(theta);
    m=new_matrix()
    ident(m)
    m[1][1]=math.cos(rad)
    m[2][1]=-math.sin(rad)
    m[1][2]=math.sin(rad)
    m[2][2]=math.cos(rad)
    return m

def make_rotY( theta ):
    rad=math.radians(theta);
    m=new_matrix()
    ident(m)
    m[0][0]=math.cos(rad)
    m[0][3]=-math.sin(rad)
    m[2][0]=math.sin(rad)
    m[2][3]=math.cos(rad)
    return m

def make_rotZ( theta ):
    rad=math.radians(theta);
    m=new_matrix()
    ident(m)
    m[0][0]=math.cos(rad)
    m[1][0]=-math.sin(rad)
    m[0][1]=math.sin(rad)
    m[1][1]=math.cos(rad)
    return m

def print_matrix( matrix ):
    s = ''
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            s+= str(matrix[c][r]) + ' '
        s+= '\n'
    print s

def ident( matrix ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            if r == c:
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):

    point = 0
    for row in m2:
        #get a copy of the next point
        tmp = row[:]

        for r in range(4):
            m2[point][r] = (m1[0][r] * tmp[0] +
                            m1[1][r] * tmp[1] +
                            m1[2][r] * tmp[2] +
                            m1[3][r] * tmp[3])
        point+= 1


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
