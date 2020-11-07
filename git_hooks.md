## git hooks

### install

You __need to__ install git hooks by running:

```bash
.githooks/install
```

### usage

After installation do some simple changes in the repo (eg. `touch f`), try to commit
and see what is happening and pay attention to the messages what you get. :) 

### info

Our git hooks are in the `.githooks` directory.

* [`post_commit`](https://github.com/sassbalint/sandbox/blob/master/.githooks/post-commit)
is run by git after commit. Our script is trivial, just prints a message.

* [`commit-msg`](https://github.com/sassbalint/sandbox/blob/master/.githooks/commit-msg)
is run by git after you have completed the current commit message.
Our script perform some checks on the format of the message.

* [`install`](https://github.com/sassbalint/sandbox/blob/master/.githooks/install)
is __not__ a real git hook, it is a simple `bash` script for making git hooks available for you. 
Why? git hooks must be in the `.git/hooks` directory.
The problem is that, being in the git inner area, this directory is __not__ part of the repo!
To be able to version control our hooks _and_ to be able to use hooks in every clone
we store our git hooks in the `.githooks` directory. 
As git hooks __must__ be accessible cia `.git/hooks` to use them,
we just convert the latter to a link to `.githooks`.

