#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/2.0.0@bincrafters/testing")


class BoostType_ErasureConan(base.BoostBaseConan):
    name = "boost_type_erasure"
    version = "1.70.0"
