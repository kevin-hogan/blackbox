service "stack" : {
	implementation : { binary : "./stack" }

	source "outport" : { integer(10) }
	sink "inport" : { integer(10) }
}

service "remstack" : {
	implementation : { binary : "/flubber/purtilo/stack_adt/stack" 
			machine : "flubber.cs.umd.edu" }

	source "outport" : { integer(10) }
	sink "inport" : { integer(10) }
}

service "priority" : {
	implementation : { binary : "./priority" }

	source "outport" : { integer(10) }
	sink "inport" : { integer(10) }
}

orchestrate "demo" : {
	tool "stack" : "remstack"
	tool "priority"
	bind "stack outport" "priority inport"
	bind "priority outport" "stack inport"
}
