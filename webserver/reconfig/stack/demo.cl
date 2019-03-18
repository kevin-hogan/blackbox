# for each of the two generic service descriptions, try switching
# around the implementation attribute to obtain the varying implementations...

service "init" : {
	implementation : { binary : "./init" }
	source "outport" : { integer(10) }
}

service "lstack" : {
	implementation : { 
		binary : "./lstack" 
#		machine : "seamster.cs.umd.edu"
	}

	source "outport" : { integer(10) }
	sink "inport" : { integer(10) }
}

service "astack" : {
	implementation : { 
		binary : "./astack" 
#		machine : "seamster.cs.umd.edu"
	}

	source "outport" : { integer(10) }
	sink "inport" : { integer(10) }
}

orchestrate "demo" : {
	tool "a" : "init"
	tool "lstack" : "lstack"
	tool "astack" : "astack"

	bind "a outport" "astack inport"
	bind "lstack outport" "astack inport"
	bind "astack outport" "lstack inport"

}



########################
#  oldies ...

service "remstack" : {
	implementation : { binary : "/flubber/purtilo/stack_adt/stack" 
			machine : "flubber.cs.umd.edu" }

	source "outport" : { integer(10) }
	sink "inport" : { integer(10) }
}

