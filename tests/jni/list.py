import jni

try:
    ArrayList = jni.cls("java/util/ArrayList")
except:
    print("SKIP")
    raise SystemExit

l = ArrayList()
print(l)
l.add_bvb("one")
l.add_bvb("two")

print(l.toString())
print(l)
print(l[0], l[1])
