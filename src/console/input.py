from colored import fg, bg, attr
import os

def consoleInput():
    return (("%s%s %s" % (fg(46), bg("green"), attr("bold")))
    + ("%s%sC%s" % (fg(46), bg("green"), attr("bold")))
    + ("%s%sM%s" % (fg(46), bg("green"), attr("bold")))
    + ("%s%sU%s" % (fg(46), bg("green"), attr("bold")))
    + ("%s%s %s" % (fg(46), bg("green"), attr("bold")))
    + ("%s%sP%s" % (fg(46), bg("green"), attr("bold")))
    + ("%s%sG%s" % (fg(46), bg("green"), attr("bold")))
    + ("%s%sP%s" % (fg(46), bg("green"), attr("bold")))
    + ("%s%s %s" % (fg(46), bg(34), attr("reset")))
    + ("%s%s %s" % (fg(46), bg(28), attr("reset")))
    + ("%s%s %s" % (fg(34), bg(22), attr("reset")))
    + ("%s%s %s" % (fg(46), bg(0), attr("reset"))))
    + ("%s%s %s" % (fg(46), bg(0), attr("reset")))
