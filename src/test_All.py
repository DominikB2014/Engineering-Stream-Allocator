## @file test_All.py
#  @title Program Unit Testing
#  @author Dominik Buszowiecki
#  @date February 9, 2019

import pytest
from SeqADT import *
from DCapALst import *
from SALst import *
from StdntAllocTypes import *


class TestSeqADT:

    def setup_method(self):
        self.new = SeqADT(["test1", "test2", "test3"])

    def teardown_method(self):
        self.new = None

    def test_empty(self):
        new = SeqADT([])
        with pytest.raises(StopIteration):
            new.next()

    def test_stop_iteration(self):
        new = SeqADT(["Test1"])
        new.next()
        with pytest.raises(StopIteration):
            new.next()

    def test_next(self):
        assert self.new.next() == "test1"

    def test_end_false(self):
        assert not self.new.end()

    def test_end_true(self):
        self.new.next()
        self.new.next()
        self.new.next()
        assert self.new.end()

    def test_start(self):
        self.new.next()
        self.new.start()
        assert self.new.next() == "test1"


class TestDCapALst:

    def setup_method(self):
        DCapALst.init()

    def teardown_method(self):
        DCapALst.s = None

    def test_constructor(self):
        DCapALst.s == []

    def test_add(self):
        DCapALst.add(DeptT.engphys, 10)
        assert DCapALst.s == [(DeptT.engphys, 10)]

    def test_add_exception(self):
        DCapALst.add(DeptT.software, 20)
        with pytest.raises(KeyError):
            DCapALst.add(DeptT.software, 30)

    def test_elm_true(self):
        DCapALst.add(DeptT.software, 10)
        assert DCapALst.elm(DeptT.software)

    def test_elm_false(self):
        DCapALst.add(DeptT.chemical, 100)
        assert not DCapALst.elm(DeptT.software)

    def test_remove(self):
        DCapALst.add(DeptT.chemical, 20)
        DCapALst.remove(DeptT.chemical)
        assert DeptT.chemical not in DCapALst.s

    def test_remove_exception(self):
        DCapALst.add(DeptT.materials, 30)
        with pytest.raises(KeyError):
            DCapALst.remove(DeptT.electrical)

    def test_capacity(self):
        DCapALst.add(DeptT.civil, 100)
        assert DCapALst.capacity(DeptT.civil) == 100

    def test_capacity_exception(self):
        DCapALst.add(DeptT.mechanical, 100)
        with pytest.raises(KeyError):
            DCapALst.capacity(DeptT.electrical)


class TestSALst:

    def setup_method(self):
        SALst.init()
        SALst.add("macid1", SInfoT("first1", "last1", GenT.male, 12.0,
                                   SeqADT([DeptT.civil, DeptT.chemical]), True))
        SALst.add("macid2", SInfoT("first2", "last2", GenT.male, 11.0,
                                   SeqADT([DeptT.civil, DeptT.chemical]), False))
        SALst.add("macid3", SInfoT("first3", "last3", GenT.male, 10.0,
                                   SeqADT([DeptT.chemical, DeptT.civil]), True))
        SALst.add("macid4", SInfoT("first4", "last4", GenT.female, 11.5,
                                   SeqADT([DeptT.civil, DeptT.chemical]), True))

    def teardown_method(self):
        SALst.s = None

    def test_constructor(self):
        SALst.init()
        assert SALst.s == []

    def test_add(self):
        SALst.init()
        sinfo1 = SInfoT("first", "last", GenT.male, 12.0,
                        SeqADT([DeptT.civil, DeptT.chemical]), True)
        SALst.add("macid1", sinfo1)
        assert SALst.s == [("macid1", sinfo1)]

    def test_add_exception(self):
        sinfo1 = SInfoT("first", "last", GenT.male, 12.0,
                        SeqADT([DeptT.civil, DeptT.chemical]), True)
        with pytest.raises(KeyError):
            SALst.add("macid1", sinfo1)

    def test_remove(self):
        SALst.remove("macid3")
        assert "macid3" not in SALst.s

    def test_remove_exception(self):
        with pytest.raises(KeyError):
            SALst.remove("macid")

    def test_elm_true(self):
        assert SALst.elm("macid1")

    def test_elm_false(self):
        assert not SALst.elm("macid")

    def test_info(self):
        sinfo = SALst.info("macid1")
        sinfo1 = SInfoT("first1", "last1", GenT.male, 12.0,
                        SeqADT([DeptT.civil, DeptT.chemical]), True)
        assert sinfo[0] == sinfo1[0]
        assert sinfo[1] == sinfo1[1]
        assert sinfo[2] == sinfo1[2]
        assert sinfo[3] == sinfo1[3]
        assert sinfo[4].next() == sinfo1[4].next() and sinfo[4].next() == sinfo1[4].next()
        assert sinfo[5] == sinfo1[5]

    def test_info_exception(self):
        with pytest.raises(KeyError):
            SALst.info("macid")

    def test_sort_empty(self):
        assert SALst.sort(lambda t: t.gpa > 12) == []

    def test_sort(self):
        assert SALst.sort(lambda t: t.freechoice and t.gpa >= 4.0) == ["macid1",
                                                                       "macid4",
                                                                       "macid3"]

    def test_average(self):
        assert SALst.average(lambda x: x.gender == GenT.male) == 11.0

    def test_average_exception(self):
        with pytest.raises(ValueError):
            assert SALst.average(lambda x: x.gpa > 12)

    def test_allocate_normal(self):
        DCapALst.init()
        DCapALst.add(DeptT.civil, 3)
        DCapALst.add(DeptT.chemical, 2)
        SALst.allocate()
        assert AALst.s == [(DeptT.civil, ["macid1", "macid4", "macid2"]),
                           (DeptT.chemical, ["macid3"]),
                           (DeptT.electrical, []),
                           (DeptT.mechanical, []),
                           (DeptT.software, []),
                           (DeptT.materials, []),
                           (DeptT.engphys, [])]

    def test_allocate_exception(self):
        DCapALst.init()
        DCapALst.add(DeptT.civil, 2)
        DCapALst.add(DeptT.chemical, 0)
        with pytest.raises(RuntimeError):
            SALst.allocate()
