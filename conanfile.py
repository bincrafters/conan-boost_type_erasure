#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/testing")

class BoostType_ErasureConan(base.BoostBaseConan):
    name = "boost_type_erasure"
    url = "https://github.com/bincrafters/conan-boost_type_erasure"
    lib_short_names = ["type_erasure"]
    options = {"shared": [True, False]}
    default_options = "shared=False"
    b2_requires = [
        "boost_assert",
        "boost_config",
        "boost_core",
        "boost_fusion",
        "boost_iterator",
        "boost_mp11",
        "boost_mpl",
        "boost_preprocessor",
        "boost_smart_ptr",
        "boost_thread",
        "boost_throw_exception",
        "boost_type_traits",
        "boost_typeof",
        "boost_vmd"
    ]
