#
# Autogenerated by Thrift Compiler (0.9.2)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
from ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class Iface:
  def getModelInformation(self):
    """
    Get information about available models
    @return Map of model name to model info
    """
    pass

  def evaluateProperties(self, entries, props):
    """
    Compute the properties of each entry in a list. Results are stored in
    the predictedProperties and classProbs maps.

    @param entries [in] List of entries to be evaluated
    @param props [in] Names of properties to evaluate
    @return Entry objects with property measurements

    Parameters:
     - entries
     - props
    """
    pass

  def searchSingleObjective(self, obj, genMethod, numToList):
    """
    Search for optimal materials based on a single objective in a
    user-defined space

         _How to Define Objective Function_

    The first word in the objective function input should be the name of the
    property being optimized, followed by whether to minimize or maximize the
    objective function, then the name of EntryRanker, and (finally) its options.

    Summary: <property> <minimize|maximize> <EntryRanker method> <options...>

    Example: To find a material with a band gap close to 1.3 eV
        bandgap minimize TargetEntryRanker 1.3

    Relevant Document Pages:

    ./javadoc/magpie/optimization/rankers/package-summary.html

         _How to Define Search Space_

    Search spaces are created using EntryGenerator classes. The first
     in the input string is the name of the generator class, which
    is followed by any options for the generator

    Summary: <EntryGenerator method> <options...>

    Example: 5 points on each binary containing either Al, Ni, or Zr
        PhaseDiagramCompositionEntryGenerator 1 2 -alloy 0.2 Al Ni Zr

    Relevant Documentation Pages:

    ./javadoc/magpie/data/utilities/generators/package-summary.html

    @param obj [in] Objective function
    @param genMethod [in] Definition of search space
    @param numToList [in] Number of top candidates to return
    @return List of the top-performing entries

    Parameters:
     - obj
     - genMethod
     - numToList
    """
    pass

  def searchMultiObjective(self, p, objs, genMethod, numToList):
    """
    Search for optimal materials based on a multiple objectives in a
    user-defined space. Combines multiple objective functions using
    the AdaptiveScalarizingEntryRanker.

    Individual objective functions are defined in the same way as in the
    single objective search.

    Relevant Documentation Pages:

    ./javadoc/magpie/optimization/rankers/AdaptiveScalarizingEntryRanker.html

    @param p [in] Tradeoff Parameter
    @param objs [in] Objective functions
    @param genMethod [in] Definition of search space
    @param numToList [in] Number of top candidates to return
    @return List of the top-performing entries

    Parameters:
     - p
     - objs
     - genMethod
     - numToList
    """
    pass


class Client(Iface):
  def __init__(self, iprot, oprot=None):
    self._iprot = self._oprot = iprot
    if oprot is not None:
      self._oprot = oprot
    self._seqid = 0

  def getModelInformation(self):
    """
    Get information about available models
    @return Map of model name to model info
    """
    self.send_getModelInformation()
    return self.recv_getModelInformation()

  def send_getModelInformation(self):
    self._oprot.writeMessageBegin('getModelInformation', TMessageType.CALL, self._seqid)
    args = getModelInformation_args()
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_getModelInformation(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = getModelInformation_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.ouch is not None:
      raise result.ouch
    raise TApplicationException(TApplicationException.MISSING_RESULT, "getModelInformation failed: unknown result");

  def evaluateProperties(self, entries, props):
    """
    Compute the properties of each entry in a list. Results are stored in
    the predictedProperties and classProbs maps.

    @param entries [in] List of entries to be evaluated
    @param props [in] Names of properties to evaluate
    @return Entry objects with property measurements

    Parameters:
     - entries
     - props
    """
    self.send_evaluateProperties(entries, props)
    return self.recv_evaluateProperties()

  def send_evaluateProperties(self, entries, props):
    self._oprot.writeMessageBegin('evaluateProperties', TMessageType.CALL, self._seqid)
    args = evaluateProperties_args()
    args.entries = entries
    args.props = props
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_evaluateProperties(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = evaluateProperties_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.ouch is not None:
      raise result.ouch
    raise TApplicationException(TApplicationException.MISSING_RESULT, "evaluateProperties failed: unknown result");

  def searchSingleObjective(self, obj, genMethod, numToList):
    """
    Search for optimal materials based on a single objective in a
    user-defined space

         _How to Define Objective Function_

    The first word in the objective function input should be the name of the
    property being optimized, followed by whether to minimize or maximize the
    objective function, then the name of EntryRanker, and (finally) its options.

    Summary: <property> <minimize|maximize> <EntryRanker method> <options...>

    Example: To find a material with a band gap close to 1.3 eV
        bandgap minimize TargetEntryRanker 1.3

    Relevant Document Pages:

    ./javadoc/magpie/optimization/rankers/package-summary.html

         _How to Define Search Space_

    Search spaces are created using EntryGenerator classes. The first
     in the input string is the name of the generator class, which
    is followed by any options for the generator

    Summary: <EntryGenerator method> <options...>

    Example: 5 points on each binary containing either Al, Ni, or Zr
        PhaseDiagramCompositionEntryGenerator 1 2 -alloy 0.2 Al Ni Zr

    Relevant Documentation Pages:

    ./javadoc/magpie/data/utilities/generators/package-summary.html

    @param obj [in] Objective function
    @param genMethod [in] Definition of search space
    @param numToList [in] Number of top candidates to return
    @return List of the top-performing entries

    Parameters:
     - obj
     - genMethod
     - numToList
    """
    self.send_searchSingleObjective(obj, genMethod, numToList)
    return self.recv_searchSingleObjective()

  def send_searchSingleObjective(self, obj, genMethod, numToList):
    self._oprot.writeMessageBegin('searchSingleObjective', TMessageType.CALL, self._seqid)
    args = searchSingleObjective_args()
    args.obj = obj
    args.genMethod = genMethod
    args.numToList = numToList
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_searchSingleObjective(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = searchSingleObjective_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.ouch is not None:
      raise result.ouch
    raise TApplicationException(TApplicationException.MISSING_RESULT, "searchSingleObjective failed: unknown result");

  def searchMultiObjective(self, p, objs, genMethod, numToList):
    """
    Search for optimal materials based on a multiple objectives in a
    user-defined space. Combines multiple objective functions using
    the AdaptiveScalarizingEntryRanker.

    Individual objective functions are defined in the same way as in the
    single objective search.

    Relevant Documentation Pages:

    ./javadoc/magpie/optimization/rankers/AdaptiveScalarizingEntryRanker.html

    @param p [in] Tradeoff Parameter
    @param objs [in] Objective functions
    @param genMethod [in] Definition of search space
    @param numToList [in] Number of top candidates to return
    @return List of the top-performing entries

    Parameters:
     - p
     - objs
     - genMethod
     - numToList
    """
    self.send_searchMultiObjective(p, objs, genMethod, numToList)
    return self.recv_searchMultiObjective()

  def send_searchMultiObjective(self, p, objs, genMethod, numToList):
    self._oprot.writeMessageBegin('searchMultiObjective', TMessageType.CALL, self._seqid)
    args = searchMultiObjective_args()
    args.p = p
    args.objs = objs
    args.genMethod = genMethod
    args.numToList = numToList
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_searchMultiObjective(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = searchMultiObjective_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.ouch is not None:
      raise result.ouch
    raise TApplicationException(TApplicationException.MISSING_RESULT, "searchMultiObjective failed: unknown result");


class Processor(Iface, TProcessor):
  def __init__(self, handler):
    self._handler = handler
    self._processMap = {}
    self._processMap["getModelInformation"] = Processor.process_getModelInformation
    self._processMap["evaluateProperties"] = Processor.process_evaluateProperties
    self._processMap["searchSingleObjective"] = Processor.process_searchSingleObjective
    self._processMap["searchMultiObjective"] = Processor.process_searchMultiObjective

  def process(self, iprot, oprot):
    (name, type, seqid) = iprot.readMessageBegin()
    if name not in self._processMap:
      iprot.skip(TType.STRUCT)
      iprot.readMessageEnd()
      x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
      oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
      x.write(oprot)
      oprot.writeMessageEnd()
      oprot.trans.flush()
      return
    else:
      self._processMap[name](self, seqid, iprot, oprot)
    return True

  def process_getModelInformation(self, seqid, iprot, oprot):
    args = getModelInformation_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = getModelInformation_result()
    try:
      result.success = self._handler.getModelInformation()
    except MagpieException, ouch:
      result.ouch = ouch
    oprot.writeMessageBegin("getModelInformation", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_evaluateProperties(self, seqid, iprot, oprot):
    args = evaluateProperties_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = evaluateProperties_result()
    try:
      result.success = self._handler.evaluateProperties(args.entries, args.props)
    except MagpieException, ouch:
      result.ouch = ouch
    oprot.writeMessageBegin("evaluateProperties", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_searchSingleObjective(self, seqid, iprot, oprot):
    args = searchSingleObjective_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = searchSingleObjective_result()
    try:
      result.success = self._handler.searchSingleObjective(args.obj, args.genMethod, args.numToList)
    except MagpieException, ouch:
      result.ouch = ouch
    oprot.writeMessageBegin("searchSingleObjective", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_searchMultiObjective(self, seqid, iprot, oprot):
    args = searchMultiObjective_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = searchMultiObjective_result()
    try:
      result.success = self._handler.searchMultiObjective(args.p, args.objs, args.genMethod, args.numToList)
    except MagpieException, ouch:
      result.ouch = ouch
    oprot.writeMessageBegin("searchMultiObjective", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()


# HELPER FUNCTIONS AND STRUCTURES

class getModelInformation_args:

  thrift_spec = (
  )

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('getModelInformation_args')
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class getModelInformation_result:
  """
  Attributes:
   - success
   - ouch
  """

  thrift_spec = (
    (0, TType.MAP, 'success', (TType.STRING,None,TType.STRUCT,(ModelInfo, ModelInfo.thrift_spec)), None, ), # 0
    (1, TType.STRUCT, 'ouch', (MagpieException, MagpieException.thrift_spec), None, ), # 1
  )

  def __init__(self, success=None, ouch=None,):
    self.success = success
    self.ouch = ouch

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.MAP:
          self.success = {}
          (_ktype44, _vtype45, _size43 ) = iprot.readMapBegin()
          for _i47 in xrange(_size43):
            _key48 = iprot.readString();
            _val49 = ModelInfo()
            _val49.read(iprot)
            self.success[_key48] = _val49
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.ouch = MagpieException()
          self.ouch.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('getModelInformation_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.MAP, 0)
      oprot.writeMapBegin(TType.STRING, TType.STRUCT, len(self.success))
      for kiter50,viter51 in self.success.items():
        oprot.writeString(kiter50)
        viter51.write(oprot)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.ouch is not None:
      oprot.writeFieldBegin('ouch', TType.STRUCT, 1)
      self.ouch.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.success)
    value = (value * 31) ^ hash(self.ouch)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class evaluateProperties_args:
  """
  Attributes:
   - entries
   - props
  """

  thrift_spec = (
    None, # 0
    (1, TType.LIST, 'entries', (TType.STRUCT,(Entry, Entry.thrift_spec)), None, ), # 1
    (2, TType.LIST, 'props', (TType.STRING,None), None, ), # 2
  )

  def __init__(self, entries=None, props=None,):
    self.entries = entries
    self.props = props

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.LIST:
          self.entries = []
          (_etype55, _size52) = iprot.readListBegin()
          for _i56 in xrange(_size52):
            _elem57 = Entry()
            _elem57.read(iprot)
            self.entries.append(_elem57)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.LIST:
          self.props = []
          (_etype61, _size58) = iprot.readListBegin()
          for _i62 in xrange(_size58):
            _elem63 = iprot.readString();
            self.props.append(_elem63)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('evaluateProperties_args')
    if self.entries is not None:
      oprot.writeFieldBegin('entries', TType.LIST, 1)
      oprot.writeListBegin(TType.STRUCT, len(self.entries))
      for iter64 in self.entries:
        iter64.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.props is not None:
      oprot.writeFieldBegin('props', TType.LIST, 2)
      oprot.writeListBegin(TType.STRING, len(self.props))
      for iter65 in self.props:
        oprot.writeString(iter65)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.entries)
    value = (value * 31) ^ hash(self.props)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class evaluateProperties_result:
  """
  Attributes:
   - success
   - ouch
  """

  thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRUCT,(Entry, Entry.thrift_spec)), None, ), # 0
    (1, TType.STRUCT, 'ouch', (MagpieException, MagpieException.thrift_spec), None, ), # 1
  )

  def __init__(self, success=None, ouch=None,):
    self.success = success
    self.ouch = ouch

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.LIST:
          self.success = []
          (_etype69, _size66) = iprot.readListBegin()
          for _i70 in xrange(_size66):
            _elem71 = Entry()
            _elem71.read(iprot)
            self.success.append(_elem71)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.ouch = MagpieException()
          self.ouch.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('evaluateProperties_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.LIST, 0)
      oprot.writeListBegin(TType.STRUCT, len(self.success))
      for iter72 in self.success:
        iter72.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.ouch is not None:
      oprot.writeFieldBegin('ouch', TType.STRUCT, 1)
      self.ouch.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.success)
    value = (value * 31) ^ hash(self.ouch)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class searchSingleObjective_args:
  """
  Attributes:
   - obj
   - genMethod
   - numToList
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'obj', None, None, ), # 1
    (2, TType.STRING, 'genMethod', None, None, ), # 2
    (3, TType.I32, 'numToList', None, None, ), # 3
  )

  def __init__(self, obj=None, genMethod=None, numToList=None,):
    self.obj = obj
    self.genMethod = genMethod
    self.numToList = numToList

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.obj = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.genMethod = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.numToList = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('searchSingleObjective_args')
    if self.obj is not None:
      oprot.writeFieldBegin('obj', TType.STRING, 1)
      oprot.writeString(self.obj)
      oprot.writeFieldEnd()
    if self.genMethod is not None:
      oprot.writeFieldBegin('genMethod', TType.STRING, 2)
      oprot.writeString(self.genMethod)
      oprot.writeFieldEnd()
    if self.numToList is not None:
      oprot.writeFieldBegin('numToList', TType.I32, 3)
      oprot.writeI32(self.numToList)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.obj)
    value = (value * 31) ^ hash(self.genMethod)
    value = (value * 31) ^ hash(self.numToList)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class searchSingleObjective_result:
  """
  Attributes:
   - success
   - ouch
  """

  thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRUCT,(Entry, Entry.thrift_spec)), None, ), # 0
    (1, TType.STRUCT, 'ouch', (MagpieException, MagpieException.thrift_spec), None, ), # 1
  )

  def __init__(self, success=None, ouch=None,):
    self.success = success
    self.ouch = ouch

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.LIST:
          self.success = []
          (_etype76, _size73) = iprot.readListBegin()
          for _i77 in xrange(_size73):
            _elem78 = Entry()
            _elem78.read(iprot)
            self.success.append(_elem78)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.ouch = MagpieException()
          self.ouch.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('searchSingleObjective_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.LIST, 0)
      oprot.writeListBegin(TType.STRUCT, len(self.success))
      for iter79 in self.success:
        iter79.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.ouch is not None:
      oprot.writeFieldBegin('ouch', TType.STRUCT, 1)
      self.ouch.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.success)
    value = (value * 31) ^ hash(self.ouch)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class searchMultiObjective_args:
  """
  Attributes:
   - p
   - objs
   - genMethod
   - numToList
  """

  thrift_spec = (
    None, # 0
    (1, TType.DOUBLE, 'p', None, None, ), # 1
    (2, TType.LIST, 'objs', (TType.STRING,None), None, ), # 2
    (3, TType.STRING, 'genMethod', None, None, ), # 3
    (4, TType.I32, 'numToList', None, None, ), # 4
  )

  def __init__(self, p=None, objs=None, genMethod=None, numToList=None,):
    self.p = p
    self.objs = objs
    self.genMethod = genMethod
    self.numToList = numToList

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.DOUBLE:
          self.p = iprot.readDouble();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.LIST:
          self.objs = []
          (_etype83, _size80) = iprot.readListBegin()
          for _i84 in xrange(_size80):
            _elem85 = iprot.readString();
            self.objs.append(_elem85)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.genMethod = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I32:
          self.numToList = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('searchMultiObjective_args')
    if self.p is not None:
      oprot.writeFieldBegin('p', TType.DOUBLE, 1)
      oprot.writeDouble(self.p)
      oprot.writeFieldEnd()
    if self.objs is not None:
      oprot.writeFieldBegin('objs', TType.LIST, 2)
      oprot.writeListBegin(TType.STRING, len(self.objs))
      for iter86 in self.objs:
        oprot.writeString(iter86)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.genMethod is not None:
      oprot.writeFieldBegin('genMethod', TType.STRING, 3)
      oprot.writeString(self.genMethod)
      oprot.writeFieldEnd()
    if self.numToList is not None:
      oprot.writeFieldBegin('numToList', TType.I32, 4)
      oprot.writeI32(self.numToList)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.p)
    value = (value * 31) ^ hash(self.objs)
    value = (value * 31) ^ hash(self.genMethod)
    value = (value * 31) ^ hash(self.numToList)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class searchMultiObjective_result:
  """
  Attributes:
   - success
   - ouch
  """

  thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRUCT,(Entry, Entry.thrift_spec)), None, ), # 0
    (1, TType.STRUCT, 'ouch', (MagpieException, MagpieException.thrift_spec), None, ), # 1
  )

  def __init__(self, success=None, ouch=None,):
    self.success = success
    self.ouch = ouch

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.LIST:
          self.success = []
          (_etype90, _size87) = iprot.readListBegin()
          for _i91 in xrange(_size87):
            _elem92 = Entry()
            _elem92.read(iprot)
            self.success.append(_elem92)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.ouch = MagpieException()
          self.ouch.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('searchMultiObjective_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.LIST, 0)
      oprot.writeListBegin(TType.STRUCT, len(self.success))
      for iter93 in self.success:
        iter93.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.ouch is not None:
      oprot.writeFieldBegin('ouch', TType.STRUCT, 1)
      self.ouch.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.success)
    value = (value * 31) ^ hash(self.ouch)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)