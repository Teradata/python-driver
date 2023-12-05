/* Copyright 2023 by Teradata Corporation. All rights reserved. */
#include <unistd.h>

void udfsleep (int *seconds, int *result, char exception[6])
{
    sleep ((unsigned int) *seconds) ;
    *result = 1 ;
}
