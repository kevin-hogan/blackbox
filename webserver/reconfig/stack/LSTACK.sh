#! /bin/bash -f

# echo LAUNCHER $*
ssh seamster ./lstack $*

#    ... but some won't work until we open firewall ...
# ssh vis ./lstack $*
