/* File: Mistral.i, generated by mk_interface.py */
%module Mistral 

%{
#include <Mistral.hpp>
#include <mistral_mod.h>
#include <mistral_glo.h>
%}

%include "src/Mistral.hpp"

%template(MistralExpArray) MistralArray< Mistral_Expression* >;
%template(MistralIntArray) MistralArray< int >;
%template(MistralDoubleArray) MistralArray< double >;

