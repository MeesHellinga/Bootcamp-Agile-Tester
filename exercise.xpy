You can implement step definitions for undefined steps with these snippets:

#Scenario
@given(u'There is an empty text file available to us')
def step_impl(conext, empty_file):
    context.empty_file = True

@when(u'I open this file')
def step_impl(context):
    context.empty_file:
        f=open("tekst.txt", "wt")
        f.close()

@when(u'I write the following table in it')
def step_impl(context, {course}, {participants}):
    for row in context.table:
        course = row["course"]
        participant = row["participants"]

@then(u'This file has 3 lines in it')
def step_impl(context):
    pass


#Scenario Outline
@given(u'The text file has been opened')
def step_impl(context):
    f=open("tekst.txt", "wt")
    f.close()

@then(u'I write the values <first>, <second> and <third>')
def step_impl(context, {first}, {second}, {third}):
    for row in context.table:
        first = row["first"]
        second = row["second"]
        third = row["third"]


@then(u'I close the file')
def step_impl(context):
    pass

