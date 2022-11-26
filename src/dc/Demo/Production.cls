Class dc.Demo.Production Extends Ens.Production
{

XData ProductionDefinition
{
<Production Name="dc.Demo.Production" TestingEnabled="true" LogGeneralTraceEvents="false">
  <Description></Description>
  <ActorPoolSize>2</ActorPoolSize>
  <Item Name="ServiceOCR" Category="" ClassName="User.ServiceOCR" PoolSize="1" Enabled="false" Foreground="false" Comment="" LogTraceEvents="false" Schedule="">
    <Setting Target="Host" Name="%settings"></Setting>
  </Item>
  <Item Name="SaveFileOperation" Category="" ClassName="User.SaveFileOperation" PoolSize="1" Enabled="true" Foreground="false" Comment="" LogTraceEvents="false" Schedule="">
    <Setting Target="Host" Name="%settings">path=/irisdev/app/misc/out</Setting>
  </Item>
</Production>
}

}
